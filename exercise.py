import requests
import json

apiKey = 'c990f8f7259b8891224f148dcdd45c94'

Maldives = 'http://api.openweathermap.org/data/2.5/forecast?id=1282028&APPID=' + apiKey

Balcones = 'http://api.openweathermap.org/data/2.5/weather?zip=78201,us&APPID=' + apiKey

Moscow = 'http://api.openweathermap.org/data/2.5/weather?id=524901&APPID=' + apiKey

SanAntonio = 'http://api.openweathermap.org/data/2.5/weather?id=4726206&APPID=' + apiKey


resp = requests.get(Balcones)

if resp.status_code in [200, 201]:
    weatherData = resp.json()
    print(
            "The weather in {} is {}.".format
         (
            weatherData['name'],
            weatherData['weather'][0]['description'])
         )


else:
    print("ERROR: " + str(resp.status_code))


resp = requests.get(SanAntonio)

if resp.status_code in [200, 201]:
    weatherData = resp.json()
    print(
            "The weather in {} is {}.".format
         (
            weatherData['name'],
            weatherData['weather'][0]['description'])
         )
else:
    print("ERROR: " + str(resp.status_code))


resp = requests.get(Moscow)

if resp.status_code in [200, 201]:
    weatherData = resp.json()
    print(
            "The weather in {} is {}.".format
         (
            weatherData['name'],
            weatherData['weather'][0]['description'])
         )
else:
    print("ERROR: " + str(resp.status_code))


response = requests.get(Maldives)
weatherData = response.json()

if response.status_code in [200, 201]:
    weatherData = response.json()

    for i in range(35):
        print(
                'On {} the weather in Republic of Maldives will be {}'.format
             (
                str(weatherData['list'][i]['dt_txt']),
                str(weatherData['list']
                [i]['weather'][0]['description'])
             )
             )

else:
    print('ERROR: ' + str(response.status_code))
