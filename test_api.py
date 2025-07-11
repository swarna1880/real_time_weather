import requests

API_KEY = "swarnakey"
city = "Delhi"
url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)
print("Status Code:", response.status_code)
print("Response:", response.text)
