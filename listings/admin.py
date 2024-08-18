from django.contrib import admin

from .models import Listing, HotelRoom, RentedHotel, RentHouse

class ListingAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')
  list_display_links = ('id', 'title')
  list_filter = ('realtor',)
  list_editable = ('is_published',)
  search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price')
  list_per_page = 25

admin.site.register(Listing, ListingAdmin)

class HotelRoomAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'is_published', 'price', 'list_date')
  list_display_links = ('id', 'title')
  list_editable = ('is_published',)
  search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price')
  list_per_page = 25

admin.site.register(HotelRoom, HotelRoomAdmin)

class RentedHotelAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'hotel_id', 'check_in', 'check_out', 'amount')
    list_filter = ('user_id', 'hotel_id')
    search_fields = ('user_id__username', 'hotel_id__hotel_name')
  
admin.site.register(RentedHotel, RentedHotelAdmin)


class RentHouseAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')
  list_display_links = ('id', 'title')
  list_filter = ('realtor',)
  list_editable = ('is_published',)
  search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price')
  list_per_page = 25

admin.site.register(RentHouse, RentHouseAdmin)