from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('studio_name', 'date', 'start_time', 'end_time', 'is_block_booking')
