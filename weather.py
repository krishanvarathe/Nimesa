import requests

API_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"


def get_weather_data():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch weather data.")
        return None


def get_temperature(data, target_time):
    for item in data['list']:
        if item['dt_txt'] == target_time:
            return item['main']['temp']
    return None


def get_wind_speed(data, target_time):
    for item in data['list']:
        if item['dt_txt'] == target_time:
            return item['wind']['speed']
    return None


def get_pressure(data, target_time):
    for item in data['list']:
        if item['dt_txt'] == target_time:
            return item['main']['pressure']
    return None


def main():
    weather_data = get_weather_data()
    if not weather_data:
        return

    while True:
        print("\nMenu:")
        print("1. Get Temperature")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            target_time = input("Enter date and time (YYYY-MM-DD HH:MM:SS): ")
            temperature = get_temperature(weather_data, target_time)
            if temperature is not None:
                print(f"Temperature at {target_time}: {temperature}°C")
            else:
                print("Temperature data not found for the specified time.")

        elif choice == '2':
            target_time = input("Enter date and time (YYYY-MM-DD HH:MM:SS): ")
            wind_speed = get_wind_speed(weather_data, target_time)
            if wind_speed is not None:
                print(f"Wind Speed at {target_time}: {wind_speed} m/s")
            else:
                print("Wind speed data not found for the specified time.")

        elif choice == '3':
            target_time = input("Enter date and time (YYYY-MM-DD HH:MM:SS): ")
            pressure = get_pressure(weather_data, target_time)
            if pressure is not None:
                print(f"Pressure at {target_time}: {pressure} hPa")
            else:
                print("Pressure data not found for the specified time.")

        elif choice == '0':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
