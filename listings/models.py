from django.db import models
from datetime import datetime, timedelta
from realtors.models import Realtor
from django.contrib.auth.models import User
from .choices import state_choices

class Listing(models.Model):

  state_choices = [
        ('AP', 'Andhra Pradesh'),
        ('AR', 'Arunachal Pradesh'),
        ('AS', 'Assam'),
        ('BR', 'Bihar'),
        ('CG', 'Chhattisgarh'),
        ('GA', 'Goa'),
        ('GJ', 'Gujarat'),
        ('HR', 'Haryana'),
        ('HP', 'Himachal Pradesh'),
        ('JK', 'Jammu and Kashmir'),
        ('JH', 'Jharkhand'),
        ('KA', 'Karnataka'),
        ('KL', 'Kerala'),
        ('MP', 'Madhya Pradesh'),
        ('MH', 'Maharashtra'),
        ('MN', 'Manipur'),
        ('ML', 'Meghalaya'),
        ('MZ', 'Mizoram'),
        ('NL', 'Nagaland'),
        ('OR', 'Orissa'),
        ('PB', 'Punjab'),
        ('RJ', 'Rajasthan'),
        ('SK', 'Sikkim'),
        ('TN', 'Tamil Nadu'),
        ('TR', 'Tripura'),
        ('UK', 'Uttarakhand'),
        ('UP', 'Uttar Pradesh'),
        ('WB', 'West Bengal'),
        ('TN', 'Tamil Nadu'),
        ('TR', 'Tripura'),
        ('AN', 'Andaman and Nicobar Islands'),
        ('CH', 'Chandigarh'),
        ('DH', 'Dadra and Nagar Haveli'),
        ('DD', 'Daman and Diu'),
        ('DL', 'Delhi'),
        ('LD', 'Lakshadweep'),
        ('PY', 'Pondicherry'),
    ]

  realtor = models.ForeignKey(Realtor, on_delete=models.CASCADE)
  title = models.CharField(max_length=200)
  address = models.CharField(max_length=200)
  city = models.CharField(max_length=100)
  state = models.CharField(max_length=100, choices=state_choices)
  zipcode = models.CharField(max_length=20)
  contact_info = models.PositiveBigIntegerField()
  description = models.TextField(blank=True)
  price = models.IntegerField()
  bedrooms = models.IntegerField()
  bathrooms = models.DecimalField(max_digits=1, decimal_places=0)
  garage = models.IntegerField(default=0)
  sqft = models.IntegerField()
  photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
  photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  is_published = models.BooleanField(default=True)
  list_date = models.DateTimeField(default=datetime.now, blank=True)
  def __str__(self):
    return self.title
  
class HotelRoom(models.Model): 
    BED_TYPES = [
        ('king', 'King'),
        ('queen', 'Queen'),
        ('twin', 'Twin'),
        # Add more bed types as needed
    ]
    state_choices = [
        ('AP', 'Andhra Pradesh'),
        ('AR', 'Arunachal Pradesh'),
        ('AS', 'Assam'),
        ('BR', 'Bihar'),
        ('CG', 'Chhattisgarh'),
        ('GA', 'Goa'),
        ('GJ', 'Gujarat'),
        ('HR', 'Haryana'),
        ('HP', 'Himachal Pradesh'),
        ('JK', 'Jammu and Kashmir'),
        ('JH', 'Jharkhand'),
        ('KA', 'Karnataka'),
        ('KL', 'Kerala'),
        ('MP', 'Madhya Pradesh'),
        ('MH', 'Maharashtra'),
        ('MN', 'Manipur'),
        ('ML', 'Meghalaya'),
        ('MZ', 'Mizoram'),
        ('NL', 'Nagaland'),
        ('OR', 'Orissa'),
        ('PB', 'Punjab'),
        ('RJ', 'Rajasthan'),
        ('SK', 'Sikkim'),
        ('TN', 'Tamil Nadu'),
        ('TR', 'Tripura'),
        ('UK', 'Uttarakhand'),
        ('UP', 'Uttar Pradesh'),
        ('WB', 'West Bengal'),
        ('TN', 'Tamil Nadu'),
        ('TR', 'Tripura'),
        ('AN', 'Andaman and Nicobar Islands'),
        ('CH', 'Chandigarh'),
        ('DH', 'Dadra and Nagar Haveli'),
        ('DD', 'Daman and Diu'),
        ('DL', 'Delhi'),
        ('LD', 'Lakshadweep'),
        ('PY', 'Pondicherry'),
    ]
    realtor = models.ForeignKey(Realtor, on_delete=models.CASCADE)

    title = models.CharField(max_length=100)
    rating = models.FloatField(default=0.0, blank=True)

    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100, choices=state_choices)
    zipcode = models.CharField(max_length=100)
    address = models.CharField(max_length=255)

    description = models.TextField()
    contact_information = models.PositiveIntegerField()

    price = models.DecimalField(max_digits=10, decimal_places=2)
    room_size = models.PositiveIntegerField()  # In square feet or meters
    no_of_beds = models.PositiveSmallIntegerField(null=True, default=1)
    bed_type = models.CharField(max_length=10, choices=BED_TYPES)
    num_bathrooms = models.PositiveIntegerField()
    
    
    has_air_conditioned = models.BooleanField(default=True)
    has_wifi = models.BooleanField(default=True)
    has_pool = models.BooleanField(default=False)
    has_gym = models.BooleanField(default=False)
    has_spa = models.BooleanField(default=False)
    has_restaurant = models.BooleanField(default=False)
    has_parking = models.BooleanField(default=False)
    has_tv = models.BooleanField(default=False)
    has_pet_friendly = models.BooleanField(default=False)
    
    embed_lnk = models.TextField(null=True)

    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Dictionary to map field names to their 'on' values
        fields_to_check = {
            'has_air_conditioned': self.has_air_conditioned,
            'has_wifi': self.has_wifi,
            'has_pool': self.has_pool,
            'has_gym': self.has_gym,
            'has_spa': self.has_spa,
            'has_restaurant': self.has_restaurant,
            'has_parking': self.has_parking,
            'has_tv': self.has_tv,
            'has_pet_friendly': self.has_pet_friendly
        }

        # Loop through the fields and convert 'on' to True for each boolean field before saving
        for field_name, field_value in fields_to_check.items():
            if field_value == 'on':
                setattr(self, field_name, True)

        # Call the actual save method to save the instance
        super(HotelRoom, self).save(*args, **kwargs)

class RentedHotel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel = models.ForeignKey(HotelRoom, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    check_in = models.DateTimeField(default=datetime.now, blank=True)
    check_out = models.DateTimeField(null=True, blank=True)
    rating = models.PositiveSmallIntegerField(null=True, blank=True)
    review = models.TextField(blank=True, null=True)
    isRated = models.BooleanField(default=False)
    reviewDate = models.DateTimeField(default=datetime.now)

    def save(self, *args, **kwargs):
        # Format check_in and check_out to store as datetime objects in the desired format
        if isinstance(self.check_in, str):
            self.check_in = datetime.strptime(self.check_in, '%Y-%m-%d %H:%M:%S')

        if isinstance(self.check_out, str):
            self.check_out = datetime.strptime(self.check_out, '%Y-%m-%d %H:%M:%S')

        super(RentedHotel, self).save(*args, **kwargs)

class RentHouse(models.Model):

  state_choices = [
        ('AP', 'Andhra Pradesh'),
        ('AR', 'Arunachal Pradesh'),
        ('AS', 'Assam'),
        ('BR', 'Bihar'),
        ('CG', 'Chhattisgarh'),
        ('GA', 'Goa'),
        ('GJ', 'Gujarat'),
        ('HR', 'Haryana'),
        ('HP', 'Himachal Pradesh'),
        ('JK', 'Jammu and Kashmir'),
        ('JH', 'Jharkhand'),
        ('KA', 'Karnataka'),
        ('KL', 'Kerala'),
        ('MP', 'Madhya Pradesh'),
        ('MH', 'Maharashtra'),
        ('MN', 'Manipur'),
        ('ML', 'Meghalaya'),
        ('MZ', 'Mizoram'),
        ('NL', 'Nagaland'),
        ('OR', 'Orissa'),
        ('PB', 'Punjab'),
        ('RJ', 'Rajasthan'),
        ('SK', 'Sikkim'),
        ('TN', 'Tamil Nadu'),
        ('TR', 'Tripura'),
        ('UK', 'Uttarakhand'),
        ('UP', 'Uttar Pradesh'),
        ('WB', 'West Bengal'),
        ('TN', 'Tamil Nadu'),
        ('TR', 'Tripura'),
        ('AN', 'Andaman and Nicobar Islands'),
        ('CH', 'Chandigarh'),
        ('DH', 'Dadra and Nagar Haveli'),
        ('DD', 'Daman and Diu'),
        ('DL', 'Delhi'),
        ('LD', 'Lakshadweep'),
        ('PY', 'Pondicherry'),
    ]

  realtor = models.ForeignKey(Realtor, on_delete=models.CASCADE)
  title = models.CharField(max_length=200)
  address = models.CharField(max_length=200)
  city = models.CharField(max_length=100)
  state = models.CharField(max_length=100, choices=state_choices)
  zipcode = models.CharField(max_length=20)
  contact_info = models.PositiveBigIntegerField()
  description = models.TextField(blank=True)
  price = models.IntegerField()
  bedrooms = models.IntegerField()
  bathrooms = models.DecimalField(max_digits=1, decimal_places=0)
  garage = models.IntegerField(default=0)
  sqft = models.IntegerField()
  photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
  photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  is_published = models.BooleanField(default=True)
  list_date = models.DateTimeField(default=datetime.now, blank=True)

  def __str__(self):
    return self.title
  