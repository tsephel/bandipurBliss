import datetime
from bandipurBliss.models import Rooms, Booking

def check_availability(room, check_in, check_out):
	available = []
	booking = Booking.objects.filter(room=room)

	for bookings in booking:
		if bookings.check_in > check_out or bookings.check_out < check_in:
			available.append(True)
		else:
			available.append(False)

	return all(available)