import pytz
import config
from datetime import datetime
from .api import post_request
from .sms import send_sms
from .util import load_stations

stations = load_stations()


def get_journey_train(daily_trains_data, start_time, end_time):

    train_leg = daily_trains_data.get("trainLegs")[0]
    train_availabilities = train_leg.get("trainAvailabilities")

    matching_trains = []

    for train_availability in train_availabilities:

        train = train_availability.get("trains")[0]

        departure_segment = train.get("segments")[0]

        departure_time = datetime.fromtimestamp(departure_segment["departureTime"] / 1000, tz=pytz.utc)
        departure_time = departure_time.astimezone(config.turkey_tz)

        if start_time <= departure_time.time() <= end_time:
            matching_trains.append({"data": train, "departure_time": departure_time})

    return matching_trains


def get_available_seats_by_class(train_data):
    available_seats_by_class = {}

    for fare_info in train_data.get("availableFareInfo", []):
        for cabin_class in fare_info.get("cabinClasses", []):
            class_name = cabin_class["cabinClass"].get("name", "Unknown")
            available_seats = cabin_class.get("availabilityCount", 0)
            available_seats_by_class[class_name] = available_seats_by_class.get(class_name, 0) + available_seats

    return available_seats_by_class


def fetch_and_filter_journeys(
    departure_station_name,
    arrival_station_name,
    desired_departure_date,
    desired_departure_start_time,
    desired_departure_end_time,
    notificated_number,
):
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {config.auth_token}",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
        "Origin": "https://ebilet.tcddtasimacilik.gov.tr",
        "Connection": "keep-alive",
        "unit-id": "3895",
    }
    params = {
        "environment": config.environment,
        "userId": config.user_id,
    }
    body = {
        "searchRoutes": [
            {
                "departureStationId": stations.get(departure_station_name),
                "departureStationName": departure_station_name,
                "arrivalStationId": stations.get(arrival_station_name),
                "arrivalStationName": arrival_station_name,
                "departureDate": desired_departure_date,
            }
        ],
        "passengerTypeCounts": [{"id": 0, "count": 1}],
        "searchReservation": False,
    }

    response = post_request(url=f"{config.base_url}{config.availability_endpoint}", body=body, headers=headers, params=params)

    if not response.status_code == 200:
        print("Hata:", response.status_code, response.text)
        return True
    else:
        data = response.json()
        matching_trains = get_journey_train(data, desired_departure_start_time, desired_departure_end_time)
        if not matching_trains:
            print("Belirtilen tarihe uygun tren bulunamadı.")
            return False
        else:
            for matching_train in matching_trains:
                available_seats_by_class = get_available_seats_by_class(matching_train["data"])
                for class_name, seats in available_seats_by_class.items():
                    if class_name == "EKONOMİ" and seats > 0:

                        sms_message = f"{departure_station_name} - {arrival_station_name} {matching_train['departure_time'].strftime('%H:%M')} - Ekonomi sınıfı {seats} boş koltuk."
                        send_sms(
                            sms_message,
                            notificated_number=notificated_number,
                        )
                        return False

    return True