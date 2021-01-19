from django.shortcuts import render
from .models import *
# Create your views here.

def Main(request):
    alliances = Alliance.objects.all()
    return render(request,'WW2/main.html', {'alliances':alliances})

def Alliance_info(request, ally_ID):
    countries = Country.objects.filter(ally_id = ally_ID)
    alliance = Alliance.objects.get(id = ally_ID)
    #name = Alliance.objects.get(id = ally_id)
    #country = Country.objects.filter(id = ally_id)
    return render(request,'WW2/alliance_info.html', {'countries':countries, 'alliance':alliance})

def Country_info(request, country_ID):
    country = Country.objects.get(id = country_ID)
    alliance = Alliance.objects.get(id = country.ally_id.id)
    weapons = Weapon.objects.filter(users__id = country_ID)
    return render(request,'WW2/country_info.html', {'country':country, 'alliance':alliance, 'weapons':weapons})

def Weapon_info(request, weapon_ID):
    weapon = Weapon.objects.get(id = weapon_ID)
    countries = weapon.users.all()
    #countries = Country.objects.filter(id__in=weapon.users)
    return render(request, 'WW2/weapon_info.html', {'weapon':weapon, 'countries':countries})