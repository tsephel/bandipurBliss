from django.shortcuts import render, HttpResponse, redirect
from .models import Rooms, Booking
from django.views.generic import FormView
from .forms import AvailabelForm
from bandipurBliss.booking_function.available import check_availability



# Create your views here.
def home_view(request):

	if request.method == "POST":
		form = AvailabelForm(request.POST or None)

		if form.is_valid():
			data = form.cleaned_data
			room_list = Rooms.objects.filter(category=data['room_category'])
			available_rooms = []

			for room in room_list:
				if check_availability(room, data['check_in'], data['check_out']):
					available_rooms.append(room)

			if len(available_rooms)>0:
				room = available_rooms[0]
				booking = Booking.objects.create(
					name = data['name'],
					room = room,
					contact = data['contact'],
					email = data['email'],
					check_in = data['check_in'],
					check_out = data['check_out']
				)
				booking.save()

				return redirect('/success/')

			else:
				return redirect('/failure/')

	else:
		form = AvailabelForm()


	context = {
		'form': form,
	}

	return render(request, "home.html", context)

def success_view(request):

	return render(request, 'success.html',)


def failure_view(request):

	return render(request, 'failure.html',)



# class BookingView(FormView):
# 	from_class = AvailabelForm
# 	template_name = 'available.html'

# 	def form_valid(self, form):
# 		data = form.cleaned_data
# 		room_list = Rooms.object.filter(category=data['room_category'])
# 		available_rooms = []

# 		for room in room_list:
# 			if check_availability(room, data['check_in'], data['check_out']):
# 				available_rooms.append(room)

# 		if len(available_rooms)>0:
# 			room = available_rooms[0]
# 			booking = Booking.object.create(
# 				user = data['name'],
# 				room = room,
# 				check_in = data['check_in'],
# 				check_out = data['check_out']
# 			)
# 			booking.save()

# 			return HttpResponse(booking)

# 		else:
# 			return HttpResponse('There are no room available')



