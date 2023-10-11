import os
import re

# Directory where your .txt files are located
folder_path = "Koprus_Pi"

# Function to clean and save data
def clean_and_save(file_path):
    # Extract the filename (excluding the path and extension)
    filename = os.path.splitext(os.path.basename(file_path))[0]

    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.read()

    # Remove "https://"
    data = data.replace("https://", "")

    # Remove "[sunting | sunting sumber]", "[1]", etc.
    data = re.sub(r'\[\d+\]', '', data)  # Removes [1], [2], ...
    data = re.sub(r'\[sunting \| sunting sumber\]', '', data)  # Removes [sunting | sunting sumber]

    # Remove non-alphanumeric characters and extra white spaces
    cleaned_data = re.sub(r'[^a-zA-Z0-9\s]', '', data)
    cleaned_data = ' '.join(cleaned_data.split())

    # Create a new file with the same filename as the original file
    cleaned_file_name = filename + ".txt"
    cleaned_file_path = os.path.join(folder_path, cleaned_file_name)
    with open(cleaned_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write(cleaned_data)

    print(f"Cleaned data saved as {cleaned_file_path}")

# Iterate over files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):
        file_path = os.path.join(folder_path, filename)
        clean_and_save(file_path)
