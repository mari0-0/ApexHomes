from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard-Hotel/', views.dashboardHotel, name='dashboard-hotel'),
    path('rate/', views.rate_hotel, name='rate_hotel'),
]
