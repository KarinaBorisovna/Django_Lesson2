import csv
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from pagination.settings import BUS_STATION_CSV



with open(BUS_STATION_CSV, 'r', encoding='utf-8') as file:
    stations_list = csv.DictReader(file) 
    station = [stat for stat in stations_list]

def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    current_page = request.GET.get('page', 1)
    paginator = Paginator(station, 10)
    page = paginator.get_page(current_page)

    context = {
        'bus_stations': page,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
