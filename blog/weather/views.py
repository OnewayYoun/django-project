from django.shortcuts import render, HttpResponse


# Create your views here.
def weather(request):
    if request.method == 'POST':
        city = request.POST['city']
    else:
        city = ''
    return render(request, 'weather.html', dict(city=city))
