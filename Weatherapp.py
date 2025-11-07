import requests

city = input("Enter the city: ")

url = f"https://api.weatherapi.com/v1/current.json?key=f45bfea7ec1a476f80b131937250611&q=bulk {city}"

response = requests.get(url)
print(response.text)

