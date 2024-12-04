import requests

def get_weather(api_key, city):
    """Fetch the weather data for a given city."""
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

def display_weather(weather_data):
    """Display the weather information."""
    if weather_data:
        city = weather_data['name']
        country = weather_data['sys']['country']
        temperature = weather_data['main']['temp']
        description = weather_data['weather'][0]['description']
        
        print(f"Weather in {city}, {country}:")
        print(f"Temperature: {temperature}°C")
        print(f"Description: {description.capitalize()}")
    else:
        print("City not found or invalid API key.")

def main():
    api_key = input("Enter your OpenWeatherMap API key: ")
    city = input("Enter the city name: ")
    
    weather_data = get_weather(api_key, city)
    display_weather(weather_data)

if __name__ == "__main__":
    main()
