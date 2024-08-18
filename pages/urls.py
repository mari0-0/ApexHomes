from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hotels', views.indexHotels, name='indexHotels'),
    path('about', views.about, name='about'),
    path('about-hotels', views.aboutHotels, name='aboutHotels'),
    path('location_city_endpoint', views.location_city_endpoint)
]
