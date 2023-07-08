import requests

api_url = 'https://api.openweathermap.org/data/2.5/weather'
city = input('please tell me ur city? - ')
params = {
    'q': city,
    'appid': '11c0d3dc6093f7442898ee49d2430d20',
    'units': 'metric'
}

res = requests.get(api_url, params=params)
# print(res.status_code)
# print(res.headers["Content-Type"])
data = res.json()
print(f"Hey! Weather in {city} is: {data['main']['temp']} it feels like: {data['main']['feels_like']} humidity is: {data['main']['humidity']}%")
