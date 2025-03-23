import requests
import json

# Endpoint URL
url = "https://cdn-api-prod-ytp.tcddtasimacilik.gov.tr/datas/stations.json?environment=dev&userId=1"

# Send POST request
response = requests.get(url)
data = response.json()

# Extract station names and IDs
stations = {station["name"]: int(station["id"]) for station in data}

# Save to JSON file
with open("stations.json", "w", encoding="utf-8") as f:
    json.dump(stations, f, ensure_ascii=False, indent=4)

print("Station names and IDs have been saved to stations.json")
