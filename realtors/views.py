from django.shortcuts import render, redirect
from .models import Realtor
from listings.choices import bedroom_choices, state_choices
from listings.models import Listing, HotelRoom, RentHouse
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.

def sell(request):
    return render(request,'realtors/sell.html')


@login_required
def sellForm(request):

    if request.method == 'POST':
        try:
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            name = first_name + ' ' + last_name
            email = request.POST['email']
            ph_no = request.POST['ph_no']
            profile_pic = request.FILES.get('profile_pic')
            house_no = request.POST['house_no']
            address = request.POST['address']
            city = request.POST['city']
            state = request.POST['state']
            postcode = request.POST['postcode']
            sqft = request.POST['sqft']
            price = request.POST['price']
            bedrooms = request.POST['bedrooms']
            bathrooms = request.POST['bathrooms']
            garages = request.POST['garages']
            imgs = request.FILES.getlist('imgs')
            description = request.POST['description']

            if (email != '') and (not User.objects.filter(email=email).exists()):
                messages.error(request, 'There is no User with this mail Create one')
                return redirect('register')          

            try:
                realtor = Realtor.objects.get(email=email)
            except:
                realtor = False
            if not realtor:
                realtor = Realtor.objects.create(
                    email=email,
                    phone = ph_no,
                    name=name,
                    photo=profile_pic
                    )
            House = Listing.objects.create(
                realtor=realtor,
                title=house_no,
                address=address,
                city=city,
                state=state,
                zipcode=postcode,
                contact_info=ph_no,
                description=description,
                price=price,
                bedrooms=bedrooms,
                bathrooms=bathrooms,
                garage=garages,
                sqft=sqft
                )
            
            for i, img in enumerate(imgs):
                if i == 0:
                    # First image goes to photo_main
                    House.photo_main = img
                elif 0 < i <= 6:
                    # Set the next 6 images to photo_1 through photo_6
                    setattr(House, f'photo_{i}', img)

            House.save()
            messages.success(request, 'You have successfully listed your House')
            return redirect('index')
        except:
            messages.error(request, 'Please Fill All Details')

        return redirect('sell-form')
    
    context = {
        'bedroom_choices': bedroom_choices,
        'state_choices':state_choices,
        'user': request.user
    }
    return render(request,'realtors/form.html', context)

#-------HOTEL-------------

def listHotel(request):
    return render(request,'realtors/rent-hotels.html')

def rentForm(request):
    if request.method == 'POST':
        try:
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            name = first_name + ' ' + last_name
            email = request.POST['email']
            ph_no = request.POST['ph_no']
            profile_pic = request.FILES.get('profile_pic')

            if (email != '') and (not User.objects.filter(email=email).exists()):
                messages.error(request, 'There is no User with this mail Create one')
                return redirect('register')    
             
            try:
                realtor = Realtor.objects.get(email=email)
            except:
                realtor = False

            if not realtor:
                realtor = Realtor.objects.create(
                    email=email,
                    phone = ph_no,
                    name=name,
                    photo=profile_pic
                    )
                
            hotel_name = request.POST['hotel_name']
            address = request.POST['address']
            city = request.POST['city']
            state = request.POST['state']
            postcode = request.POST['postcode']
            sqft = request.POST['sqft']
            price = request.POST['price']
            bedrooms = request.POST['bedrooms']
            bathrooms = request.POST['bathrooms']
            bed_type = request.POST['bed_type']
            ac = request.POST.get('ac', False)
            wifi = request.POST.get('wifi', False)
            pool = request.POST.get('pool', False)
            gym = request.POST.get('gym', False)
            spa = request.POST.get('spa', False)
            restaurant = request.POST.get('restaurant', False)
            parking = request.POST.get('parking', False)
            tv = request.POST.get('tv', False)
            pet = request.POST.get('pet', False)
            imgs = request.FILES.getlist('imgs')
            description = request.POST['description']

            Hotel = HotelRoom.objects.create(
                realtor=realtor,
                title=hotel_name,
                city=city,
                state=state,
                zipcode=postcode,
                address=address,
                description=description,
                contact_information=ph_no,
                price=price,
                no_of_beds=bedrooms,
                num_bathrooms=bathrooms,
                room_size=sqft,
                bed_type=bed_type,
                has_air_conditioned=ac,
                has_wifi=wifi,
                has_pool=pool,
                has_gym=gym,
                has_spa=spa,
                has_restaurant=restaurant,
                has_parking=parking,
                has_tv=tv,
                has_pet_friendly=pet
            )
            for i, img in enumerate(imgs):
                if i == 0:
                    # First image goes to photo_main
                    Hotel.photo_main = img
                elif 0 < i <= 6:
                    # Set the next 6 images to photo_1 through photo_6
                    setattr(Hotel, f'photo_{i}', img)

            Hotel.save()
            messages.success(request, 'You have successfully listed your Hotel')
            return redirect('indexHotels')
        except:
            messages.error(request, 'Please Fill All Details')
    
        return redirect('rent-form')
    

    context = {
        'bedroom_choices': bedroom_choices,
        'state_choices':state_choices,
        'bed_type': HotelRoom.BED_TYPES,
        'user': request.user

    }

    return render(request, 'realtors/form-hotels.html', context)


def rentHouse(request):
    
    if request.method == 'POST':
        try:
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            name = first_name + ' ' + last_name
            email = request.POST['email']
            ph_no = request.POST['ph_no']
            profile_pic = request.FILES.get('profile_pic')
            house_no = request.POST['house_no']
            address = request.POST['address']
            city = request.POST['city']
            state = request.POST['state']
            postcode = request.POST['postcode']
            sqft = request.POST['sqft']
            price = request.POST['price']
            bedrooms = request.POST['bedrooms']
            bathrooms = request.POST['bathrooms']
            garages = request.POST['garages']
            imgs = request.FILES.getlist('imgs')
            description = request.POST['description']

            if (email != '') and (not User.objects.filter(email=email).exists()):
                messages.error(request, 'There is no User with this mail Create one')
                return redirect('register')          

            try:
                realtor = Realtor.objects.get(email=email)
            except:
                realtor = False
            if not realtor:
                realtor = Realtor.objects.create(
                    email=email,
                    phone = ph_no,
                    name=name,
                    photo=profile_pic
                    )
            House = RentHouse.objects.create(
                realtor=realtor,
                title=house_no,
                address=address,
                city=city,
                state=state,
                zipcode=postcode,
                contact_info=ph_no,
                description=description,
                price=price,
                bedrooms=bedrooms,
                bathrooms=bathrooms,
                garage=garages,
                sqft=sqft
                )
            
            for i, img in enumerate(imgs):
                if i == 0:
                    # First image goes to photo_main
                    House.photo_main = img
                elif 0 < i <= 6:
                    # Set the next 6 images to photo_1 through photo_6
                    setattr(House, f'photo_{i}', img)

            House.save()
            messages.success(request, 'You have successfully listed your House')
            return redirect('index')
        except:
            messages.error(request, 'Please Fill All Details')

        return redirect('sell-form')
    

    context = {
        'bedroom_choices': bedroom_choices,
        'state_choices':state_choices,
        'user': request.user
    }
    return render(request, 'realtors/form-rent.html', context)