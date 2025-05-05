import pytz
from datetime import datetime

# Variables
turkey_tz = pytz.timezone("Europe/Istanbul")
utc_tz = pytz.utc
environment = "dev"
user_id = 1
auth_token = """eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJlVFFicDhDMmpiakp1cnUzQVk2a0ZnV196U29MQXZIMmJ5bTJ2OUg5THhRIn0.eyJleHAiOjE3MjEzODQ0NzAsImlhdCI6MTcyMTM4NDQxMCwianRpIjoiYWFlNjVkNzgtNmRkZS00ZGY4LWEwZWYtYjRkNzZiYjZlODNjIiwiaXNzIjoiaHR0cDovL3l0cC1wcm9kLW1hc3RlcjEudGNkZHRhc2ltYWNpbGlrLmdvdi50cjo4MDgwL3JlYWxtcy9tYXN0ZXIiLCJhdWQiOiJhY2NvdW50Iiwic3ViIjoiMDAzNDI3MmMtNTc2Yi00OTBlLWJhOTgtNTFkMzc1NWNhYjA3IiwidHlwIjoiQmVhcmVyIiwiYXpwIjoidG1zIiwic2Vzc2lvbl9zdGF0ZSI6IjAwYzM4NTJiLTg1YjEtNDMxNS04OGIwLWQ0MWMxMTcyYzA0MSIsImFjciI6IjEiLCJyZWFsbV9hY2Nlc3MiOnsicm9sZXMiOlsiZGVmYXVsdC1yb2xlcy1tYXN0ZXIiLCJvZmZsaW5lX2FjY2VzcyIsInVtYV9hdXRob3JpemF0aW9uIl19LCJyZXNvdXJjZV9hY2Nlc3MiOnsiYWNjb3VudCI6eyJyb2xlcyI6WyJtYW5hZ2UtYWNjb3VudCIsIm1hbmFnZS1hY2NvdW50LWxpbmtzIiwidmlldy1wcm9maWxlIl19fSwic2NvcGUiOiJvcGVuaWQgZW1haWwgcHJvZmlsZSIsInNpZCI6IjAwYzM4NTJiLTg1YjEtNDMxNS04OGIwLWQ0MWMxMTcyYzA0MSIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwicHJlZmVycmVkX3VzZXJuYW1lIjoid2ViIiwiZ2l2ZW5fbmFtZSI6IiIsImZhbWlseV9uYW1lIjoiIn0.AIW_4Qws2wfwxyVg8dgHRT9jB3qNavob2C4mEQIQGl3urzW2jALPx-e51ZwHUb-TXB-X2RPHakonxKnWG6tDIP5aKhiidzXDcr6pDDoYU5DnQhMg1kywyOaMXsjLFjuYN5PAyGUMh6YSOVsg1PzNh-5GrJF44pS47JnB9zk03Pr08napjsZPoRB-5N4GQ49cnx7ePC82Y7YIc-gTew2baqKQPz9_v381Gbm2V38PZDH9KldlcWut7kqQYJFMJ7dkM_entPJn9lFk7R5h5j_06OlQEpWRMQTn9SQ1AYxxmZxBu5XYMKDkn4rzIIVCkdTPJNCt5PvjENjClKFeUA1DOg"""
base_url = "https://web-api-prod-ytp.tcddtasimacilik.gov.tr"
availability_endpoint = "/tms/train/train-availability"

# SMS and call settings from Twilio API (please refer to https://console.twilio.com)
twilio_auth_token = "" 
twilio_account_sid = ""
twilio_number = ""

# Notification types to be used. Options: sms, call, win11
# WARNING: If you use sms, Twilio will charge you for each SMS sent. If you use call, it won't charge you as long as you don't answer the call.
notification_types = ["win11"] # Edit this to enable SMS or call notifications. For example: ["sms", "call", "win11"]

# Journey details (check stations.json for valid station names)
departure_station_name = "İSTANBUL(SÖĞÜTLÜÇEŞME)"
arrival_station_name = "ANKARA GAR"
desired_departure_date = turkey_tz.localize(datetime(2025, 5, 6, 0, 0, 0)).astimezone(utc_tz).strftime("%d-%m-%Y %H:%M:%S")
desired_departure_start_time = datetime.strptime("19:20", "%H:%M").time()
desired_departure_end_time = datetime.strptime("19:40", "%H:%M").time()
notificated_number = ""

# Wait time between checks in seconds
sleep_time = 30
