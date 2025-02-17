import requests

def get_city(lat=61.2500, lon=73.4167):
    api_key = "YOUR_API_KEY"
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
    headers = {'weather': 'description', 'main': 'pressure', 'main': 'humidity', 'sys': 'name'}
    response = requests.get(url)
    # print(response.json())
    response = response.json()
    return f"City name: {response['name']}\nweather: {response['weather'][0]['description']}\npressure: {response['main']['pressure']}\nhumidity: {response['main']['humidity']}"

print(get_city())