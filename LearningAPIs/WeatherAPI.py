import requests

API_KEY = "b026cb5d00d4db8e9813f7b7a51ce97f"

BASE_URL = "http://api.openweathermap.org/data/2.5/weather"


def get_weather_data(city):
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None


def display_weather(data):
    if data:
        city = data['name']
        country = data['sys']['country']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        weather_description = data['weather'][0]['description']

        print(f"Weather in {city}, {country}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {weather_description.capitalize()}")
    else:
        print("City not found or invalid response from the server.")


def main():
    print("Welcome to the Python Weather App!")

    while True:
        city = input("\nEnter the name of a city to check the weather (or type 'exit' to quit): ").strip()

        if city.lower() == 'exit':
            print("Goodbye!")
            break

        weather_data = get_weather_data(city)
        display_weather(weather_data)


if __name__ == "__main__":
    main()
