import datetime
import time

def convert_to_linux_time(date_str, time_str):
    try:
        # Parse date and time strings
        date_obj = datetime.datetime.strptime(f"{date_str} {time_str}", "%d/%m/%Y %H:%M")

        # Convert to timestamp
        timestamp = int(date_obj.timestamp())
        return timestamp

    except ValueError:
        print("Invalid date or time format. Please use dd/mm/yyyy and hh:mm.")
        return None

if __name__ == "__main__":
    date_input = input("Enter date (dd/mm/yyyy): ")
    time_input = input("Enter time (hh:mm): ")

    linux_timestamp = convert_to_linux_time(date_input, time_input)

    if linux_timestamp is not None:
        print(f"Linux timestamp: {linux_timestamp}")

    # Example usage with hardcoded values
    date_input_hardcoded = "25/12/2023"
    time_input_hardcoded = "12:30"

    linux_timestamp_hardcoded = convert_to_linux_time(date_input_hardcoded, time_input_hardcoded)

    if linux_timestamp_hardcoded is not None:
        print(f"Hardcoded Linux timestamp: {linux_timestamp_hardcoded}")
