from django import forms
from .models import Payment

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ('full_name', 'email', 'phone_number', 'street_address1',
                  'street_address2', 'town_or_city', 'county', 'country', 'postcode')
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Full Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Phone Number'}),
            'street_address1': forms.TextInput(attrs={'placeholder': 'Street Address 1'}),
            'street_address2': forms.TextInput(attrs={'placeholder': 'Street Address 2'}),
            'town_or_city': forms.TextInput(attrs={'placeholder': 'Town or City'}),
            'county': forms.TextInput(attrs={'placeholder': 'County'}),
            'country': forms.TextInput(attrs={'placeholder': 'Country'}),
            'postcode': forms.TextInput(attrs={'placeholder': 'Postcode'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email',
            'phone_number': 'Phone Number',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'town_or_city': 'Town or City',
            'county': 'County',
            'country': 'Country',
            'postcode': 'Postcode',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'form form-control mt-3'
            self.fields[field].label = False
