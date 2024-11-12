# Weather API Project To-Do List (Using FastAPI)

## 1. Set Up the Project Environment
- [x] Create a new GitHub repo for the project. Maybe call it `weather-api-project` or something similar.
- [x] Clone the new repo to my local machine so I can start working.
- [x] Set up a virtual environment using `venv` to keep things organized.
- [x] Activate the virtual environment to get ready for package installations.

## 2. Install the Packages I Need
- [x] Install FastAPI: `pip install fastapi` (the framework I’ll be using).
- [x] Install Uvicorn: `pip install uvicorn` (to run the FastAPI app).
- [x] Install requests: `pip install requests` (for making HTTP requests to the weather API).
- [x] Install Redis and the Python Redis client: `pip install redis` (for caching).
- [x] Install python-dotenv: `pip install python-dotenv` (to manage environment variables).
- [ ] (Optional) If I need rate limiting later, I can look into installing a package for that.

## 3. Set Up the Project Structure
- [x] Make a main folder to keep all my project files organized.
- [x] Inside that folder, create `app.py` for the main FastAPI app.
- [ ] Set up a `.env` file to store sensitive stuff like API keys.
- [ ] Create a `requirements.txt` file to keep track of all my dependencies.

## 4. Build the Basic FastAPI App
- [ ] Write a simple FastAPI app in `app.py` with a route that returns hardcoded weather data.
- [ ] Run and test the app locally using: `uvicorn app:app --reload` to make sure it works.

## 5. Set Up Redis for Caching
- [ ] Install Redis on my computer following the guide for my operating system.
- [ ] Start the Redis server and make sure it’s running.
- [ ] Test the Redis connection with a basic Python script to confirm it works.

## 6. Configure Environment Variables
- [ ] Add my Visual Crossing API key to the `.env` file and use `python-dotenv` to load it in the app.
- [ ] Add the Redis connection info to `.env` as well and ensure the app can access it.

## Error Handling and Rate Limiting
- [ ] Think through how I want to handle errors, like when the weather API doesn’t respond or there’s bad input.
- [ ] If I decide to add rate limiting, research the best package and set some rules.