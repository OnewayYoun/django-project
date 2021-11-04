from django.shortcuts import render, HttpResponse
from onewayy.hide import get_secrets
import requests


# Create your views here.
def weather(request):
    api_key = get_secrets('OpenWeather_API_KEY')
    if request.method == 'POST':
        city = request.POST['city']
        base_url = 'https://api.openweathermap.org/data/2.5/weather'
        r = requests.get(f'{base_url}', params=dict(q=city, appid=api_key, units='metric'))
        if r.status_code == 200:
            res = r.json()
            data = dict(
                temp=str(res['main']['temp']) + 'C',
                pressure=str(res['main']['pressure']),
                humidity=str(res['main']['humidity']),
                coordinate=str(res['coord']['lon']) + ', ' + str(res['coord']['lat']),
                country_code=str(res['sys']['country']),
            )
        else:
            message = 'Invalid City Name. Please try again'
            return render(request, 'weather.html', dict(message=message))
    else:
        city = ''
        data = {}

    return render(request, 'weather.html', dict(city=city, data=data))
