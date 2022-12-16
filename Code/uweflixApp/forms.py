from django import forms
from uweflixApp.models import Club, MonthlyStatement

class ClubForm(forms.ModelForm):
    class Meta:
        model = Club
        fields = ['clubName', 'cardNum', 'expDate', 'discountRate',]

class MonthlyStatementForm(forms.ModelForm):
    class Meta:
        model = MonthlyStatement
        fields = ['clubID', 'date', 'amount',]