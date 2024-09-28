from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import price_choices, bedroom_choices, state_choices, hotel_price_choices, rating_choices
from django.db.models import Q
from django.http import JsonResponse
from django.contrib import messages
from datetime import datetime, timedelta
from .models import Listing, HotelRoom, RentedHotel, RentHouse
from django.db.models import Avg


def index(request):
    listings = Listing.objects.order_by("-list_date").filter(is_published=True)

    paginator = Paginator(listings, 6)
    page = request.GET.get("page")
    paged_listings = paginator.get_page(page)

    context = {"listings": paged_listings}

    return render(request, "listings/listings.html", context)


def Hotelindex(request):
    listings = HotelRoom.objects.order_by("-list_date").filter(is_published=True)

    paginator = Paginator(listings, 6)
    page = request.GET.get("page")
    paged_listings = paginator.get_page(page)

    context = {"listings": paged_listings}

    return render(request, "listings/listings-hotels.html", context)


def RentHouseIndex(request):
    listings = RentHouse.objects.order_by("-list_date").filter(is_published=True)

    paginator = Paginator(listings, 6)
    page = request.GET.get("page")
    paged_listings = paginator.get_page(page)

    context = {"listings": paged_listings}

    return render(request, "listings/rent-house-listings.html", context)



def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {"listing": listing}

    return render(request, "listings/listing.html", context)


def HotleListing(request, listing_id):
    listing = get_object_or_404(HotelRoom, pk=listing_id)
    current_date = datetime.now().strftime('%Y-%m-%d')
    one_month = (datetime.now() + timedelta(days=30)).strftime('%Y-%m-%d')
    try:
        reviews = RentedHotel.objects.filter(hotel=listing_id).order_by('check_out')
    except:
        reviews = False
    context = {
        "listing": listing,
        'current_date': current_date,
        'one_month': one_month,
        'reviews': reviews
        }

    return render(request, "listings/hotel-listing.html", context)

def RentHouseListing(request, listing_id):
    listing = get_object_or_404(RentHouse, pk=listing_id)

    context = {"listing": listing}

    return render(request, "listings/rent-house-listing.html", context)


def search(request):
    queryset_list = Listing.objects.order_by("-list_date")
    # Keywords
    if "keywords" in request.GET:
        keywords = request.GET["keywords"]
        if keywords:
            queryset_list = queryset_list.filter(
                Q(description__icontains=keywords)
                | Q(title__icontains=keywords)
                | Q(address__icontains=keywords)
                | Q(zipcode__icontains=keywords)
            )

    # City
    if "city" in request.GET:
        city = request.GET["city"]
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

    # State
    if "state" in request.GET:
        state = request.GET["state"]
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)

    # Bedrooms
    if "bedrooms" in request.GET:
        bedrooms = request.GET["bedrooms"]
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

    if "min_price" in request.GET:
        price = request.GET["min_price"]
        if price:
            queryset_list = queryset_list.filter(price__gte=price)

    # Price
    if "price" in request.GET:
        price = request.GET["price"]
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    queryset_list = queryset_list.order_by('price')
    context = {
        "state_choices": state_choices,
        "bedroom_choices": bedroom_choices,
        "price_choices": price_choices,
        "listings": queryset_list,
        "values": request.GET,
    }

    return render(request, "listings/search.html", context)


def Hotels_search(request):
    queryset_list = HotelRoom.objects.order_by("-list_date")
    # Keywords
    if "Hkeywords" in request.GET:
        keywords = request.GET["Hkeywords"]
        if keywords:
            queryset_list = queryset_list.filter(
                Q(description__icontains=keywords)
                | Q(title__icontains=keywords)
                | Q(address__icontains=keywords)
                | Q(zipcode__icontains=keywords)
            )

    # City
    if "Hcity" in request.GET:
        city = request.GET["Hcity"]
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

    # State
    if "Hstate" in request.GET:
        state = request.GET["Hstate"]
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)

    if "rating" in request.GET:
        rating = request.GET["rating"]
        if rating:
            queryset_list = queryset_list.order_by("rating").filter(rating__lte=rating)[::-1]

    # price
    if "min_price" in request.GET:
        price = request.GET["min_price"]
        if price:
            queryset_list = queryset_list.filter(price__gte=price)

    # Price
    if "max_price" in request.GET:
        price = request.GET["max_price"]
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    context = {
        "state_choices": state_choices,
        "price_choices": hotel_price_choices,
        "listings": queryset_list,
        "values": request.GET,
    }

    return render(request, "listings/hotels-search.html", context)


# views.py


def payment(request):
    if request.method == "POST":
        messages.success(request, "Payment Successful")
        
        user = request.user
        listing_id = request.POST['listing_id']
        hotel = HotelRoom.objects.get(id=listing_id)
        amount = request.POST['amount']
        check_in_str = request.POST['check_in'].replace('midnight', '12:00 AM').replace('Sept.', 'Sep.')
        check_out_str = request.POST['check_out'].replace('midnight', '12:00 AM').replace('Sept.', 'Sep.')
        
        check_in = datetime.strptime(check_in_str, '%b. %d, %Y, %I:%M %p')
        check_out = datetime.strptime(check_out_str, '%b. %d, %Y, %I:%M %p')
        
        rented = RentedHotel.objects.create(user=user, hotel=hotel, check_in=check_in, check_out=check_out, amount=amount)
        rented.save()
        return redirect("dashboard-hotel")

    listing_id = request.GET["listing_id"]
    listing = HotelRoom.objects.get(id=listing_id)
    check_in = datetime.strptime(request.GET['check_in'], '%Y-%m-%d')  # Convert to datetime object
    check_out = datetime.strptime(request.GET['check_out'], '%Y-%m-%d')  # Convert to datetime object

    # Calculate the number of days between check_in and check_out
    days = (check_out - check_in).days
    
    context = {
        "listing": listing,
        "check_in": check_in,
        "check_out": check_out,
        'days': days
    }
    return render(request, "listings/payment.html", context)
