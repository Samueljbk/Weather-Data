import os
import requests
from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

app = FastAPI()

@app.get("/weather")
async def get_weather(city: str):
    api_key = os.getenv("VISUAL_CROSSING_API_KEY")
    base_url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline"
    full_url = f"{base_url}/{city}?key={api_key}"

    try:
        response = requests.get(full_url)
        response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)
        data = response.json()
        return {
            "city": city,
            "temperature": data["currentConditions"]["temp"],
            "description": data["currentConditions"]["conditions"]
        }
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
