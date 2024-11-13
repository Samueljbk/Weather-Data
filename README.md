# Weather API 🌦️

Welcome to the **Weather API** project! This simple yet powerful API provides current weather information for cities around the world, leveraging real-time data from the [Visual Crossing Weather API](https://www.visualcrossing.com/weather-api). It also utilizes **Redis** for efficient caching to ensure fast responses and reduced API calls.

## Project Overview

This project was built as a learning exercise and a portfolio piece to demonstrate my understanding of:
- Building and structuring a **FastAPI** application.
- Integrating and fetching data from a **3rd-party API**.
- Implementing **Redis** for in-memory caching to improve performance.
- Following **best practices** for error handling and environment variable management.

The main goal was to develop a functional and optimized API while deepening my understanding of modern backend development techniques.

## Features 🚀

- **Get Current Weather**: Fetches real-time weather data for a given city.
- **Caching with Redis**: Stores data for 12 hours to speed up repeat requests and minimize external API usage.
- **Error Handling**: Provides user-friendly error messages for invalid city names, missing API keys, and network issues.
- **Automatic Documentation**: FastAPI’s built-in Swagger UI and ReDoc make it easy to understand and interact with the API.

## Technologies Used 🛠️

- **Python**: The core programming language used for development.
- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python 3.7+.
- **Redis**: Used as an in-memory data structure store for caching.
- **requests**: A simple, yet powerful HTTP library for making API requests.
- **dotenv**: For managing environment variables securely.

## How It Works 🔍

1. **Make a Request**: Clients can request weather data for a specific city using the `/weather` endpoint.
2. **Check the Cache**: The API first checks Redis to see if the data for the city is already cached.
3. **Fetch Fresh Data**: If the data is not cached or has expired, the API fetches fresh data from the Visual Crossing API.
4. **Cache and Return**: The new data is cached in Redis and returned to the client.

## Example Request & Response

**Endpoint**: `/weather?city=London`

**Sample Response**:
```json
{
  "city": "London",
  "temperature": 50.9,
  "description": "Partially cloudy"
}

### Prerequisites
- **Python 3.7+**: Make sure you have Python installed on your system.
- **Redis**: Ensure that Redis is installed and running on your local machine.