import requests 

def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        wind = data['wind']
        weather_description = data['weather'][0]['description']

        print(f"Cuaca di {city.capitalize()}:")
        print(f"Suhu: {main['temp']}°C")
        print(f"Tekanan Udara: {main['pressure']} hPa")
        print(f"Kelembapan: {main['humidity']}%")
        print(f"Kecepatan Angin: {wind['speed']} m/s")
        print(f"Deskripsi Cuaca: {weather_description.capitalize()}")
    else:
        print(f"Error {response.status_code}: Tidak dapat mengambil data cuaca untuk {city}.")


    api_key = "97ed86b99fdcf738c7a080e0fa9fde20"
    city = input("Masukkan nama kota: ")
    get_weather(city, api_key)