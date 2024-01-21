import redis
import json

# Replace these values with your Redis Cloud database connection details
host = "redis-11392.c299.asia-northeast1-1.gce.cloud.redislabs.com"
port = 11392
password = "pQ0YUG35i0DmdWk2UaBHk3uh5527IwfM"
db_index = 0  # Replace with your desired database index

# Connect to the Redis Cloud database
r = redis.Redis(host=host, port=port, password=password, decode_responses=True, db=db_index)

# Load JSON data from a file
file_path = "./items.json"  # Update with your file path
with open(file_path, "r") as file:
    json_data = file.read()

# Convert JSON to Python dictionary
data_dict = json.loads(json_data)

# Iterate through the list of lost items and store them in the Redis database
for item in data_dict["lostItems"]:
    # Using HMSET for structured data
    key = f"lostItem:{item['itemName']}"
    r.hset(key, mapping=item)
