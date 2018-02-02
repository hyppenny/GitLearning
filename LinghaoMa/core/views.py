from django.shortcuts import render


def emission(request):
    return render(request, 'core/emission.html')


def monitor(request):
    return render(request, 'core/monitor.html')


def stations(request):
    return render(request, 'core/station.html')


def about(request):
    return render(request, 'core/about.html')
