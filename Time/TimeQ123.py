# ---------- Question 1 ----------

from datetime import datetime

now = datetime.now()
print(f"The current time in Ireland is {now.strftime('%H:%M:%M')}")


# ---------- Question 2 ----------

# pip install tzdata
from zoneinfo import ZoneInfo

now_NY = datetime.now(ZoneInfo('America/New_York'))
print(f"The current time in New York is {now_NY.strftime('%H:%M:%M')}")


# ---------- Question 3 ----------

import re

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

def since_midnight(dt: datetime):
    return (dt.hour * 60 * 60 + dt.minute * 60 + dt.second)

# ----------------------------------------

user_time = ask_for_time()
now_secs = since_midnight(datetime.now())
user_secs = since_midnight(user_time)

print(f"TIme diference from now is {round((user_secs - now_secs)/60)} minutes")
