from datetime import datetime
from datetime import timedelta
import re
from num2words import num2words
from text_to_speech import speak

def ask_for_time():
    time_ok = False
    while not time_ok:
        user_input = input("Enter a time in 24-hour format [HH:MM]: ")
        time_ok  = (re.search("^[0-2]?[0-9]:[0-5][0-9]$", user_input) is not None)
        if time_ok:
            try:
                the_time = datetime.strptime(user_input, '%H:%M')
            except ValueError:
                print("Oops! That was not a valid time.")
                time_ok = False
    return the_time

# ----------------------------------------

def time_to_words(the_time):
    hour = the_time.hour
    minute = the_time.minute
    hour_str = ""

    remainder = minute % 5
    match remainder:
        case 0:
            minute_prefix = "exactly "
        case 1 | 2:
            minute_prefix = "just after "
            delta = timedelta(minutes=(-remainder))
        case 3 | 4:
            minute_prefix = "almost "
            delta = timedelta(minutes=(5-remainder))

    if remainder > 0:
        new_time = the_time + delta
        hour = new_time.hour
        minute = new_time.minute


    if minute <= 30:
        minute_dir = "past"
    else:
        minute_dir = "to"
        hour += 1
        minute = 60 - minute

    if hour == 0 or hour == 24:
        hour = 0
        hour_str = "midnight"
        am_pm = ""
    elif hour == 12:
        hour_str = "noon"
        am_pm = ""
    elif hour < 12:
        am_pm = " in the morning"
    elif hour < 18:
        am_pm = " in the afternoon"
        hour -= 12
    else:
        am_pm = " in the evening"
        hour -= 12

    if hour_str == "":
        hour_str = num2words(hour)

    if minute == 0:
        if hour != 0 and hour != 12:
            hour_str += " o'clock"
        min_str = ""
    elif minute == 15:
        min_str = "quarter " + minute_dir + " "
    elif minute == 30:
        min_str = "half " + minute_dir + " "
    else:
        min_str = num2words(minute) + " minutes " + minute_dir + " "

    return (f"{minute_prefix}{min_str}{hour_str}{am_pm}")

# ----------------------------------------

user_time = ask_for_time()
user_time_str = time_to_words(user_time)
print(f"The time is {user_time_str}")
speak(f"The time is {user_time_str}")
