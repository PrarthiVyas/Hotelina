from django import forms
from .models import *

# Create your forms here.

class AvailableForm(forms.Form):
	ROOM_CATEGORIES={
        ('AC','AC'),
        ('NON_AC','NON-AC'),
        ('DELUX','DELUX')
    }
	room_category=forms.ChoiceField(choices=ROOM_CATEGORIES,required=True)
	check_in=forms.DateTimeField(required=True,input_formats=["%Y-%m-%dT%H:%M",])
	check_out=forms.DateTimeField(required=True,input_formats=["%Y-%m-%dT%H:%M",])
