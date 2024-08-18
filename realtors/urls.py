from django.urls import path

from . import views

urlpatterns = [
    path('sell-house/', views.sell, name='sell'),
    path('sell-house-form/', views.sellForm, name='sell-form'),
    path('list-your-hotel/', views.listHotel, name='rent'),
    path('list-your-hotel-form/', views.rentForm, name='rent-form'),
    path('rent-your-house-form/', views.rentHouse, name='rent-house'),

]
