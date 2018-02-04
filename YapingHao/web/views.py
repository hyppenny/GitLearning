from django.shortcuts import render


# Create your views here.


def home(request):
    return render(request, 'home.html')


def stations(request):
    return render(request, 'Stations.html')


def emission(request):
    return render(request, 'Emission.html')


def monitor(request):
    return render(request, 'Monitor.html')


def about(request):
    return render(request, 'About.html')
