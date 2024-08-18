from django.urls import path

from . import views

urlpatterns = [
    path('Houses', views.index, name='listings'),
    path('Hotels', views.Hotelindex, name='hotels'),
    path('<int:listing_id>', views.listing, name='listing'),
    path('Hotels/<int:listing_id>', views.HotleListing, name='HotelListing'),
    path('rent-houses/<int:listing_id>', views.RentHouseListing, name='RentHouseListing'),
    path('search', views.search, name='search'),
    path('hotels-search', views.Hotels_search, name='hotels-search'),
    path('rent-houses/', views.RentHouseIndex, name='rent-houses'),
    path('process-payment/', views.payment, name='process_payment'),


]
