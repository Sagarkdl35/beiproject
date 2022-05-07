from django.contrib import admin
from .models import Booking, Dealer,Vehicle


# Register your models here.
admin.site.register(Dealer)
admin.site.register(Vehicle)
admin.site.register(Booking)

