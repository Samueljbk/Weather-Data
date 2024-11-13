import redis
import os
from dotenv import load_dotenv
import redis.exceptions

load_dotenv()

redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST"),
    port=int(os.getenv("REDIS_PORT")),
    db=int(os.getenv("REDIS_DB"))
)

try:
    redis_client.ping()
    print("success")
except redis.exceptions.ConnectionError as e:
    print(f"uh oh spaghetti-o's: {e}")