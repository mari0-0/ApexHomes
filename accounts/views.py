from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact, RentContact
from listings.models import Listing, HotelRoom, RentedHotel, RentHouse
from realtors.models import Realtor
from django.db.models import Avg
from datetime import datetime
from itertools import chain


def register(request):
  if request.method == 'POST':
    # Get form values
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']

    # Check if passwords match
    if password == password2:
      # Check username
      if User.objects.filter(username=username).exists():
        messages.error(request, 'That username is taken')
        return redirect('register')
      else:
        if User.objects.filter(email=email).exists():
          messages.error(request, 'That email is being used')
          return redirect('register')
        else:
          # Looks good
          user = User.objects.create_user(username=username, password=password,email=email, first_name=first_name, last_name=last_name)
          user.save()
          messages.success(request, 'You are now registered and can log in')
          return redirect('login')
    else:
      messages.error(request, 'Passwords do not match')
      return redirect('register')
  else:
    return render(request, 'accounts/register.html')

def login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    
    user = auth.authenticate(username=username, password=password)

    if user is not None:
      auth.login(request, user)
      messages.success(request, 'You are now logged in')
      return redirect('dashboard')
    else:
      messages.error(request, 'Invalid credentials')
      return redirect('login')
  else:
    return render(request, 'accounts/login.html')

def logout(request):
  if request.method == 'POST':
    auth.logout(request)
    messages.success(request, 'You are now logged out')
    return redirect('index')

def dashboard(request):
  user_contacts1 = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
  user_contacts2 = RentContact.objects.order_by('-contact_date').filter(user_id=request.user.id)
  user_contacts = list(chain(user_contacts1, user_contacts2))
  try:
    realtor = Realtor.objects.get(email=request.user.email)
  except:
    realtor = None
  self_contacts = Contact.objects.filter(realtor=realtor)
  rent_contacts = RentContact.objects.filter(realtor=realtor)

  combined_contacts = list(chain(self_contacts, rent_contacts))

  Houses = Listing.objects.order_by('-list_date').filter(realtor=realtor)
  RentHouses = RentHouse.objects.order_by('-list_date').filter(realtor=realtor)

  Hotels = HotelRoom.objects.order_by('-list_date').filter(realtor=realtor)
  rented = RentedHotel.objects.filter(user=request.user)
  context = {
    'contacts': user_contacts,
    'houses': Houses,
    'rent_houses': RentHouses,
    'hotels': Hotels,
    'rented': rented,
    'self_contacts': combined_contacts,
  }
  return render(request, 'accounts/dashboard.html', context)


def dashboardHotel(request):
  user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
  try:
    realtor = Realtor.objects.get(email=request.user.email)
  except:
    realtor = None
  Houses = Listing.objects.order_by('-list_date').filter(realtor=realtor)
  Hotels = HotelRoom.objects.order_by('-list_date').filter(realtor=realtor)
  rented = RentedHotel.objects.filter(user=request.user)
  context = {
    'contacts': user_contacts,
    'houses': Houses,
    'hotels': Hotels,
    'rented': rented
  }
  return render(request, 'accounts/dashboard-hotels.html', context)


def rate_hotel(request):
    # Get the hotel instance
    rentHotelId = request.GET['hotel_id_test']
    hotel = RentedHotel.objects.get(id=rentHotelId)
    
    rating = request.GET.get('rate', 0)
    review = request.GET.get('review', '')

    hotel.rating = rating
    hotel.review = review
    hotel.isRated = True
    hotel.reviewDate = datetime.now()
    hotel.save()

    update_hotel_room_rating(hotel.hotel.id)

    return redirect('dashboard')


def update_hotel_room_rating(hotel_room_id):
    # Get the specific HotelRoom instance
    hotel_room = HotelRoom.objects.get(id=hotel_room_id)

    # Get all the RentedHotel instances associated with the hotel room
    rented_hotels = RentedHotel.objects.filter(hotel=hotel_room_id)

    # Calculate the average rating for the hotel room based on associated rented hotels' ratings
    average_rating = rented_hotels.aggregate(avg_rating=Avg('rating'))['avg_rating']

    # Update the HotelRoom's average rating
    hotel_room.rating = average_rating
    hotel_room.save()

