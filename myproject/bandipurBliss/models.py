from django.db import models

# Create your models here.

class Rooms(models.Model):
	CATEGORY = (
		('BASIC', 'BASIC'),
		('DELUX', 'DELUX'),
		('PREMINUM', 'PRENIMUM'),
	)
	room_num = models.IntegerField()
	category = models.CharField(max_length=9, choices=CATEGORY)
	beds = models.IntegerField()
	capacity = models.IntegerField()
	price = models.IntegerField(null=True)

	def __str__(self):
		return f'{self.category} room number {self.room_num} with {self.beds} beds for {self.capacity} people'


class Booking(models.Model):
	name = models.CharField(max_length=100)
	room = models.ForeignKey(Rooms, on_delete = models.CASCADE)
	check_in = models.DateField()
	check_out = models.DateField()
	contact = models.CharField(max_length=100, null=True)
	email = models.EmailField(max_length=100, null=True)

	def __str__(self):
		return f"{self.name} has booked {self.room}"
