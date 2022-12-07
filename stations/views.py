from django.shortcuts import render, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.urls import reverse
import csv

def read_csv(fileName):

    return_list = []

    with open(fileName, newline= '',encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            return_list.append({'Name':row['Name'],'Street':row['Street'],'District':row['District']})
    return return_list

def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    station_list = read_csv('./data-398-2018-08-30.csv')

    page_number = int(request.GET.get('page',1))
    paginator = Paginator(station_list,10)
    page = paginator.get_page(page_number)

    try:
        station_list_page = paginator.page(page)
    except PageNotAnInteger:
        station_list_page = paginator.page(1)
    except EmptyPage:
        station_list_page = paginator.page(paginator.num_pages)

    context = {
         'bus_stations': station_list_page,
         'page': page,
    }
    return render(request, 'stations/index.html', context)
