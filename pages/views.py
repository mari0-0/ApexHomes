from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, JsonResponse
from listings.choices import price_choices, bedroom_choices, state_choices, rating_choices, hotel_price_choices
from django.views.decorators.csrf import csrf_exempt
import json
from listings.models import Listing, HotelRoom
from realtors.models import Realtor

def index(request):
    city = request.COOKIES.get('city')
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    nearby_listings = listings.filter(city__iexact=city)[:3]


    context = {
        'listings': listings,
        'nearby_listings': nearby_listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
    }
    return render(request, 'pages/index.html', context)

def indexHotels(request):
    city = request.COOKIES.get('city')

    hotels = HotelRoom.objects.order_by('-list_date').filter(is_published=True)
    nearby_hotels = hotels.filter(city__iexact=city)[:3]

    context = {
        'hotels': hotels,
        'nearby_hotels': nearby_hotels,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': hotel_price_choices,
        'rating_choices': rating_choices
    }
    return render(request, 'pages/index-hotels.html', context)



def about(request):
    # Get all realtors
    realtors = Realtor.objects.order_by('-hire_date')

    # Get MVP
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }

    return render(request, 'pages/about.html', context)

def aboutHotels(request):
    # Get all realtors
    realtors = Realtor.objects.order_by('-hire_date')

    # Get MVP
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }

    return render(request, 'pages/about-hotels.html', context)


@csrf_exempt
def location_city_endpoint(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))  # Parse the JSON data from the request body
        city = data.get('city')  # Access the 'city' data from the JSON object
        
        if city:
            # Process the city data here
            response = JsonResponse({'message': 'City data received by Django'})
            response.set_cookie('city', city)
            return response
        else:
            return JsonResponse({'error': 'No city data received'})

    else:
        return JsonResponse({'error': 'Invalid request method'})