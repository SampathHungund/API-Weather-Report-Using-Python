import requests

def get_weather_data(api_key, city_name):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "celcius"
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error fetching weather data")
        return None

def analyze_weather(weather_data):
    if weather_data:
        main_data = weather_data['main']
        weather = weather_data['weather'][0]
        wind = weather_data['wind']

        temperature = main_data['temp']
        humidity = main_data['humidity']
        description = weather['description']
        wind_speed = wind['speed']

        print(f"Weather in {weather_data['name']}, {weather_data['sys']['country']}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Description: {description.capitalize()}")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        print("Weather data is unavailable.")

if __name__ == "__main__":
    api_key = "paste your api key here"
    city_name = input("Enter the name of the city: ")

    weather_data = get_weather_data(api_key, city_name)

    analyze_weather(weather_data)
