from django import forms
from .models import RationCard, FamilyMember, Complaint

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class RationCardForm(forms.ModelForm):
    class Meta:
        model = RationCard
        fields = ['card_type', 'fair_price_shop']
        widgets = {
            'card_type': forms.Select(attrs={'class': 'form-control'}),
            'fair_price_shop': forms.Select(attrs={'class': 'form-control'}),
        }

class FamilyMemberForm(forms.ModelForm):
    class Meta:
        model = FamilyMember
        fields = ['name', 'age', 'gender', 'relationship', 'aadhar_number']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'relationship': forms.TextInput(attrs={'class': 'form-control'}),
            'aadhar_number': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['subject', 'description', 'ration_card']
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'ration_card': forms.Select(attrs={'class': 'form-control'}),
        }
