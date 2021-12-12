from django import forms
from .models import Prediction, Reservation


class ReserveForm(forms.ModelForm):
    class Meta:
        model = Reservation
        exclude = []

class PredictionForm(forms.ModelForm):
    class Meta:
        model = Prediction
        exclude = ['monday_BF',
                   'monday_LH',
                   'monday_DN',
                   'tuesday_BF',
                   'tuesday_LH',
                   'tuesday_DN',
                   'wednesday_BF',
                   'wednesday_LH',
                   'wednesday_DN',
                   'thursday_BF',
                   'thursday_LH',
                   'thursday_DN',
                   'friday_BF',
                   'friday_LH',
                   'friday_DN',
                   'saturday_BF',
                   'saturday_LH',
                   'saturday_DN',
                   'sunday_BF',
                   'sunday_LH',
                   'sunday_DN',
                   'user'
                   'id']
