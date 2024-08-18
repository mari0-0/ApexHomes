from django.urls import path

from . import views

urlpatterns = [
  path('contact', views.contact, name='contact'),
  path('rent_contact', views.Rent_contact, name='RentContact')
]