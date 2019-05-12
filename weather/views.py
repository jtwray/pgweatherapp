import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm


def index(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&APPID=71b53f142da1d82499350633e1ec5757'

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()


    form = CityForm()

    cities = City.objects.all()

    weather_data = []

    for city in cities:

        r = requests.get(url.format(city)).json()
        
        city_weather = {
            'city': city.name, 
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'], 
            'icon' : r['weather'][0]['icon'],
        }

        weather_data.append(city_weather)

    context = {'weather_data' :weather_data, 'form' : form}
    
    return render(request, 'weather/weather.html', context)

# def solarIndex(request):
#     # url = 'https://developer.nrel.gov/api/alt-fuel-stations/v1.json?fuel_type=E85,ELEC&state=CA&limit=2&api_key=be0rTxQ6CnnQ6h3CwYpBDBsQ7mdt1bTNoWmk3thr&format=JSON'
#     city = 'Asheville '
#     url='https://developer.nrel.gov/api/solar/solar_resource/v1.json?&api_key=be0rTxQ6CnnQ6h3CwYpBDBsQ7mdt1bTNoWmk3thr&format=JSON&address=30225jeb+stuart+hwy+spencer+va+24165'

#     r = requests.get(url.format(city)).json()

#     print(r)
#     return render(request, 'weather/solarIndex.html')