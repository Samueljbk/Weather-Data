import os
import requests
import redis
from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

app = FastAPI()

redis_client = redis.Redis(host='localhost', port=6379,)

@app.get("/weather")
async def get_weather(city: str):
    api_key = os.getenv("VISUAL_CROSSING_API_KEY")
    base_url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline"
    full_url = f"{base_url}/{city}?key={api_key}"

    # Check if data for the city is already in the cache
    cached_data = redis_client.get(city)
    if cached_data:
        # If cached data exists -> return it
        return eval(cached_data) # Convert string back to dictionary

    try:
        response = requests.get(full_url)
        response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)
        data = response.json()
        weather_info =  {
            "city": city,
            "temperature": data["currentConditions"]["temp"],
            "description": data["currentConditions"]["conditions"]
        }

        #12 hour expiration for cached weather data (in seconds)
        redis_client.setex(city, 12 * 60 * 60, str(weather_info))
        return weather_info
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

