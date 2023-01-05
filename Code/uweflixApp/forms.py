from django import forms
from uweflixApp.models import Club, MonthlyStatement, UserAccount

class ClubForm(forms.ModelForm):
    class Meta:
        model = Club
        fields = ['clubName', 'cardNum', 'expDate', 'discountRate',]
        labels = {
            'clubName': ('Club Name'),
            'cardNum': ('Card Number'),
            'expDate': ('Expiration Date'),
            'discountRate': ('Discount Rate'),
        }

class MonthlyStatementForm(forms.ModelForm):
    class Meta:
        model = MonthlyStatement
        fields = ['clubID', 'date', 'amount',]
        labels = {
            'clubID': ('Club ID'),
            'date': ('Date'),
            'amount': ('Amount'),
        }

class UserAccountForm(forms.ModelForm):
    class Meta:
        model = UserAccount
        fields = ['userName', 'password',]
        labels = {
            'userName': ('User Name'),
            'password': ('Password'),
        }