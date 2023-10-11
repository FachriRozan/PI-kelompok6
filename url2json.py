import json

# Read data from the "url.txt" file
data = []
with open('linkdanjudul.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

url = None
title = None

for line in lines:
    line = line.strip()
    if line.startswith("URL: "):
        if url is not None and title is not None:
            data.append({"url": url, "title": title})
        url = line.replace("URL: ", "")
    elif line.startswith("Judul: "):
        title = line.replace("Judul: ", "")

# Append the last entry to data
if url is not None and title is not None:
    data.append({"url": url, "title": title})

# Convert data to a JSON format
json_data = json.dumps(data, ensure_ascii=False, indent=4)

# Save the JSON data to a file
with open('data.json', 'w', encoding='utf-8') as json_file:
    json_file.write(json_data)
