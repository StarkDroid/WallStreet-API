import os
import shutil
from PIL import Image

source_folder = r"C:\Users\gamer\Downloads\new wallpaper"
enhance_folder = os.path.join(source_folder, "need-enhance")

os.makedirs(enhance_folder, exist_ok=True)

for filename in os.listdir(source_folder):
    file_path = os.path.join(source_folder, filename)
    
    try:
        with Image.open(file_path) as img:
            width, height = img.size
            
            if width < 900 and height < 1920:
                shutil.move(file_path, os.path.join(enhance_folder, filename))
                print(f"Moved: {filename} (Resolution: {width}x{height})")
    
    except Exception as e:
        print(f"Skipping: {filename} (Error: {e})")

print("Processing complete!")