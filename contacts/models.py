from django.db import models
from datetime import datetime
from realtors.models import Realtor

class Contact(models.Model):
  listing = models.CharField(max_length=200)
  listing_id = models.IntegerField()
  realtor = models.ForeignKey(Realtor, on_delete=models.CASCADE)
  name = models.CharField(max_length=200)
  email = models.CharField(max_length=100)
  phone = models.CharField(max_length=100)
  message = models.TextField(blank=True)
  contact_date = models.DateTimeField(default=datetime.now, blank=True)
  user_id = models.IntegerField(blank=True)

  def __str__(self):
    return self.name

class RentContact(models.Model):
  listing = models.CharField(max_length=200)
  listing_id = models.IntegerField()
  realtor = models.ForeignKey(Realtor, on_delete=models.CASCADE)
  name = models.CharField(max_length=200)
  email = models.CharField(max_length=100)
  phone = models.CharField(max_length=100)
  message = models.TextField(blank=True)
  contact_date = models.DateTimeField(default=datetime.now, blank=True)
  user_id = models.IntegerField(blank=True)

  def __str__(self):
    return self.name