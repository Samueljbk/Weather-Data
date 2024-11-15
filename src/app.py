import os
import requests
import redis
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

app = FastAPI()

redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST"),
    port=int(os.getenv("REDIS_PORT")),
    db=int(os.getenv("REDIS_DB"))
)

@app.get("/weather")
async def get_weather(city: str):
    api_key = os.getenv("VISUAL_CROSSING_API_KEY")
    if not api_key:
        return JSONResponse(
            status_code=500,
            content={"error:" "Missing API key for Visual Crossing"}
        )
    
    base_url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline"
    full_url = f"{base_url}/{city}?key={api_key}"

    # Check if data for the city is already in the cache
    cached_data = redis_client.get(city)
    if cached_data:
        print("Using cached data for: ", city)
        # If cached data exists -> return it
        return eval(cached_data) # Convert string back to dictionary
    
    print("Fetching new data for: ", city)

    try:
        response = requests.get(full_url)
        if response.status_code == 400:
            return JSONResponse(
                status_code=404,
                content={"error": f"City '{city}' not found. Please check the city name and try again."}
            )
        response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)
        data = response.json()

        if "currentConditions" not in data:
            return JSONResponse(
                status_code=404,
                content={"error": "City not found or invalid response from API"}
            )
        
        weather_info =  {
            "city": city,
            "temperature": data["currentConditions"]["temp"],
            "description": data["currentConditions"]["conditions"]
        }

        #12 hour expiration for cached weather data (in seconds)
        redis_client.setex(city, 12 * 60 * 60, str(weather_info))
        return weather_info
    
    except requests.exceptions.RequestException:
        return JSONResponse(
            status_code=500,
            content={"error": "Error fetching data from the weather service."}
        )
    except redis.exceptions.RedisError:
        return JSONResponse(
            status_code=500,
            content={"error": "Error connecting to the caching service."}
        )