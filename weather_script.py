import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

if __name__ == "__main__":
    api_key = "b6a50053476a7111416bc4397fb3108f"  # Replace with your OpenWeatherMap API key
    city = "London"
    weather_data = get_weather(api_key, city)
    if weather_data:
        print(weather_data)
    else:
        print("Failed to fetch weather data")