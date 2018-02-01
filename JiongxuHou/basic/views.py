from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views import generic
from basic.models import Navigation


def stations(request):
    navigations = get_list_or_404(Navigation)
    return render(request, template_name='basic/stations.html', context={'navigations': navigations})


def emission(request):
    navigations = get_list_or_404(Navigation)
    return render(request, template_name='basic/emission.html', context={'navigations': navigations})


def monitor(request):
    navigations = get_list_or_404(Navigation)
    return render(request, template_name='basic/monitor.html', context={'navigations': navigations})


def about(request):
    navigations = get_list_or_404(Navigation)
    return render(request, template_name='basic/about.html', context={'navigations': navigations})
