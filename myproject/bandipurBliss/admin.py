from django.contrib import admin
from .models import Rooms, Booking

# Register your models here.
# class RoomAdmin(admin.ModelAdmin):
#     class Meta:
#         model = IncomeExpense

admin.site.register(Rooms)
admin.site.register(Booking)
