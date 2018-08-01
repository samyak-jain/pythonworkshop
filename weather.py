import requests

location = input("Enter your city: ")
response1 = requests.get(f"https://www.metaweather.com/api/location/search/?query={location}").json()[0]
woeid = response1['woeid']
response2 = requests.get(f"https://www.metaweather.com/api/location/{woeid}/").json()
weather = response2['consolidated_weather'][0]["weather_state_name"]

print(weather)
