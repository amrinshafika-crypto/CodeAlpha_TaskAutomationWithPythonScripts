import os
import shutil

source_folder = "source"
destination_folder = "destination"

if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)


for file_name in os.listdir(source_folder):

    # Check if file ends with .jpg
    if file_name.endswith(".jpg"):

        source_path = os.path.join(source_folder, file_name)
        destination_path = os.path.join(destination_folder, file_name)

        shutil.move(source_path, destination_path)

        print(f"Moved: {file_name}")

print("All JPG files moved successfully!")