import json


def load_stations():
    with open("stations.json", "r", encoding="utf-8") as f:
        return json.load(f)


def turkce_ascii(text):
    replacements = {
        "İ": "I",
        "ı": "i",
        "Ş": "S",
        "ş": "s",
        "Ğ": "G",
        "ğ": "g",
        "Ü": "U",
        "ü": "u",
        "Ö": "O",
        "ö": "o",
        "Ç": "C",
        "ç": "c",
    }
    for tr, en in replacements.items():
        text = text.replace(tr, en)
    return text
