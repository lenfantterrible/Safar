from django.contrib import admin
from .models import Flight, Agency, City


admin.site.register(Agency)
admin.site.register(City)



@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = ['agency', 'origin', 'destination']
    list_filter = ['origin', 'destination', 'starts', 'arrives']
    

