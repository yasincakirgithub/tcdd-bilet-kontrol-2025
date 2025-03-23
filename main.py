import sys

sys.dont_write_bytecode = True

from src.functions import fetch_and_filter_journeys
import config
import time


def main():

    # Journey details (check stations.json for valid station names)
    departure_station_name = config.departure_station_name
    arrival_station_name = config.arrival_station_name
    desired_departure_date = config.desired_departure_date
    desired_departure_start_time = config.desired_departure_start_time
    desired_departure_end_time = config.desired_departure_end_time
    notificated_number = config.notificated_number
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
