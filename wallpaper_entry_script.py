import os
import json
from pathlib import Path

# Paths to your directories
desktop_dir = Path("desktop")
mobile_dir = Path("mobile")

# Path to your JSON file
json_file = Path("wallpapers.json")

# Load existing JSON data
if json_file.exists():
    with open(json_file, "r") as f:
        data = json.load(f)
else:
    data = {"desktop": [], "mobile": []}

# Function to add new entries
def update_json(directory, platform):
    for image_file in directory.iterdir():
        if image_file.is_file() and image_file.suffix.lower() in [".png", ".jpg", ".jpeg", ".webp"]:
            image_name = image_file.name

            # Check if the image already exists in the JSON
            exists = any(entry["imageUrl"].endswith(image_name) for entry in data[platform])
            if not exists:
                thumbnail_name = f"{image_file.stem}.webp"
                thumbnail_url = f"https://starkdroid.github.io/WallStreet-API/{platform}/thumbnail/{thumbnail_name}"

                # Create new entry
                new_entry = {
                    "category": "",
                    "imageUrl": f"https://starkdroid.github.io/WallStreet-API/{platform}/{image_name}",
                    "thumbnailUrl": thumbnail_url
                }
                data[platform].append(new_entry)
                print(f"Added new entry: {new_entry}")

# Update desktop entries
update_json(desktop_dir, "desktop")

# Update mobile entries
update_json(mobile_dir, "mobile")

# Save updated JSON data
with open(json_file, "w") as f:
    json.dump(data, f, indent=2)

print("JSON file updated successfully.")