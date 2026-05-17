import json
import os

MEMORY_FILE = "memory/data.json"

# Create file if missing
if not os.path.exists(MEMORY_FILE):
    with open(MEMORY_FILE, "w") as f:
        json.dump({}, f)

# Save memory
def save_memory(key, value):

    with open(MEMORY_FILE, "r") as f:
        data = json.load(f)

    data[key] = value

    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f, indent=4)

# Load memory
def load_memory(key):

    with open(MEMORY_FILE, "r") as f:
        data = json.load(f)

    return data.get(key, "I don't remember that.")

# Show all memory
def show_memory():

    with open(MEMORY_FILE, "r") as f:
        data = json.load(f)

    return data
