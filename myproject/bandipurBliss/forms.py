from django import forms


class DateInput(forms.DateInput):
	input_type = 'date'

class AvailabelForm(forms.Form):
	CATEGORY = (
		('BASIC', 'BASIC'),
		('DELUX', 'DELUX'),
		('PREMINUM', 'PRENIMUM'),
	)
	name = forms.CharField(max_length=100)
	room_category = forms.ChoiceField(choices=CATEGORY)
	check_in = forms.DateField(widget=DateInput)
	check_out = forms.DateField(widget=DateInput)
	contact = forms.CharField(max_length=100)
	email = forms.EmailField(max_length=100)

