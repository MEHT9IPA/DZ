from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include 
from . import views

urlpatterns = [
    path('', views.Main , name='main'),
    path('alliance_info/<int:ally_ID>/', views.Alliance_info, name='alliance_info'),
    path('country_info/<int:country_ID>/', views.Country_info, name='country_info'),
    path('weapon_info/<int:weapon_ID>/', views.Weapon_info, name='weapon_info'),
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)