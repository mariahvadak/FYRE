from django.shortcuts import render
from django.http import HttpResponse
from ceom.flux.models import TowerSite
from datetime import datetime

import csv

def index(request):
    return render(request, 'flux/index.html')

def siteselect(request):
    # data={}
    # sites = TowerSite.objects.values('id', 'name', 'lat', 'lon')
    # markers = [{'lat': site.lat, 'lng': site.lon, 'name': site.name, 'url': f'/site/{site.id}/'} for site in sites]
    # data = {'marker': markers}

    return render(request, 'flux/siteselect.html')

def recentsite(request):
    #figure this out

    return render(request, 'flux/recentsite.html')  

def site(request):
    #figure this out

    return render(request, 'flux/site.html')  

def upload(request):
    if request.method == 'POST' and request.FILES:
        csv_data = request.FILES['csv_file']

        towersite_list = []
        csv_reader = csv.reader(csv_data)
        for row in csv_reader:
            towersite_name, lat, lon = row[0], row[1], row[2]
            towersite = TowerSite.objects.create(
                user=request.user,
                towersite_name=towersite_name,
                date_uploaded=datetime.date.today(),
                lat=lat,
                lon=lon,
                csv_data=csv_data,
            )

    return render(request, 'flux/upload.html')

def download(request):
    return render(request, 'flux/download.html')  

def site_csv(request):
    # figure out csv
    sites = TowerSite.objects.filter()

    response = HttpResponse(content_type='text/csv')
    writer = csv.writer(response)

    #Header
    writer.writerow(['Tower Site', 'Longitude', 'Latitude'])

    for d in sites:
        writer.writerow([d.towersite_name, d.lon, d.lat])

    return response

def simulation(request):
    #figure this out

    return render(request, 'flux/simulation.html')
