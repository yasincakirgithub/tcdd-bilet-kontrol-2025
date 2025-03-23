import json


def load_stations():
    with open("stations.json", "r", encoding="utf-8") as f:
        return json.load(f)
