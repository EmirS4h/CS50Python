import re
import sys


def main():
    print(convert("9 PM to 5:00 AM"))
    print(convert("9 AM to 5:00 PM"))
    print(convert("9:00 PM 5:00 AM"))

# 9:00 AM to 5:00 PM
# 9 AM to 5 PM
# 9:00 PM to 5:00 AM


# def convert(time: str) -> str:
#     # if matches := re.search(
#     #         r"^(\d{1,2}:\d{0,2} AM|\d{1,2} AM) to (\d{1,2}:\d{0,2} PM|\d{1,2} PM)", time, flags=re.IGNORECASE):
#     #     print(matches.groups())
#     if matches := re.search(r'(\d{1,2})(?::(\d{2}))?\s*([ap][m])?', time, re.IGNORECASE):
#         print(matches.groups())
#     else:
#         print("Incorrect format")


def convert(time: str) -> str:
    # Define the regular expression pattern to match the time string
    pattern = r'(\d{1,2})(?::(\d{2}))?\s*([ap][m])?'

    try:
        # Use the pattern to extract the start and end times from the input string
        start_match = re.match(pattern, time, flags=re.IGNORECASE)
        end_match = re.match(pattern, time.split(' to ')
                             [1], flags=re.IGNORECASE)
    except (ValueError, IndexError):
        sys.exit("Invalid format")
    # Convert the start and end times to 24-hour format
    start_hour = int(start_match.group(1))
    start_minute = int(start_match.group(2) or 0)
    start_meridiem = start_match.group(3).lower()

    end_hour = int(end_match.group(1))
    end_minute = int(end_match.group(2) or 0)
    end_meridiem = end_match.group(3).lower()

    if start_meridiem == 'pm' and start_hour != 12:
        start_hour += 12
    elif start_meridiem == 'am' and start_hour == 12:
        start_hour = 0

    if end_meridiem == 'pm' and end_hour != 12:
        end_hour += 12
    elif end_meridiem == 'am' and end_hour == 12:
        end_hour = 0

    # Format the start and end times as 24-hour format strings
    start_time = f'{start_hour:02}:{start_minute:02}'
    end_time = f'{end_hour:02}:{end_minute:02}'

    return f'{start_time} to {end_time}'


if __name__ == "__main__":
    main()
