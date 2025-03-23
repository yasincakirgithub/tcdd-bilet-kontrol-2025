import sys

sys.dont_write_bytecode = True

from src.functions import fetch_and_filter_journeys
import config
import time
from datetime import datetime


def main():

    # Journey details (check stations.json for valid station names)
    departure_station_name = "ERYAMAN YHT"
    arrival_station_name = "ESKİŞEHİR"
    desired_departure_date = config.turkey_tz.localize(datetime(2025, 3, 28, 0, 0, 0)).astimezone(config.utc_tz).strftime("%d-%m-%Y %H:%M:%S")
    desired_departure_start_time = datetime.strptime("18:04", "%H:%M").time()
    desired_departure_end_time = datetime.strptime("18:04", "%H:%M").time()
    notificated_number = "+905077225688"
    keep_searching = True

    while keep_searching:
        print(f"### Started checking.")
        keep_searching = fetch_and_filter_journeys(
            departure_station_name=departure_station_name,
            arrival_station_name=arrival_station_name,
            desired_departure_date=desired_departure_date,
            desired_departure_start_time=desired_departure_start_time,
            desired_departure_end_time=desired_departure_end_time,
            notificated_number=notificated_number,
        )
        print(f"### Completed checking.")

        if keep_searching:
            print(f"### Will restart in {config.sleep_time} seconds.")
            time.sleep(config.sleep_time)


if __name__ == "__main__":
    main()
