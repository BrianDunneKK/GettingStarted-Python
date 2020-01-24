import pyowm
from datetime import datetime, timedelta

loc = 'Kilkenny,Ireland'

owm = pyowm.OWM('f8c5ed2d5acaf51d22e984cb02a99d7a')
observation = owm.weather_at_place(loc)
w = observation.get_weather()
wi = w.get_wind()                  # {'speed': 4.6, 'deg': 330}
hm = w.get_humidity()              # 87
tm = w.get_temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}

print(w)
print(wi)
print(hm)
print(tm)

f3 = owm.three_hours_forecast(loc)
# fd = owm.daily_forecast(loc)              # Your API subscription level does not allow to perform this operation
# fh =  owm.weather_history_at_place(loc)   # Your API subscription level does not allow to perform this operation

print("\nForecast:")
for fcast in f3._forecast._weathers:
    ref_time = fcast.get_reference_time(timeformat='iso')
    temp = fcast.get_temperature(unit='celsius')["temp"]
    details = fcast.get_detailed_status()
    desc = " {}  {:4.1f}°C  {}".format(ref_time, temp, details)
    print(desc)


# COUNTRY = 'UK'
# forecast = owm.daily_forecast('london,uk')
# forecast_date = datetime.now() + timedelta(days = 1, hours = 3)
# weather = forecast.get_weather_at(forecast_date)
# description = weather.get_detailed_status()
# clouds = weather.get_clouds()
# temperature = weather.get_temperature()
# wind = weather.get_wind()
# rain = weather.get_rain()

# print(forecast)