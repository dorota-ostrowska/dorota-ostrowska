import requests, json
import os

WEATHER_KEY = os.getenv("WEATHER_KEY")
my_api_key = WEATHER_KEY
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = "Warsaw"
complete_url = base_url + "appid=" + my_api_key + "&q=" + city_name
response = requests.get(complete_url)
x = response.json()
if x["cod"] != "404":
	y = x["main"]
	current_temperature = y["temp"]
	current_pressure = y["pressure"]
	current_humidity = y["humidity"]
	z = x["weather"]
	weather_description = z[0]["description"]
	info = ("(Updating every day at about 1 pm)\n\nTemperature 🌡️: " +
					str(current_temperature) + " K, " + str(round((current_temperature - 273.15), 2)) + "°C\n"
		    "\nAtmospheric pressure 💨: " +
					str(current_pressure) + " hPa\n"
		    "\nHumidity 💦: " +
					str(current_humidity) + "%\n"
		    "\nWeather ☔️: " +
					str(weather_description)) + "\n\n"
else:
	print(" City Not Found ")
	
with open('raw_text.txt', 'r', encoding="utf-8") as file:
    raw_text = file.read()

complete_text = raw_text + info + "</details>"

with open('README.md', 'w', encoding="utf-8") as f:
    f.write(complete_text)
