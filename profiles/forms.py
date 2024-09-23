from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

        field_order = [
            'fname',
            'lname',
            'street_address1',
            'street_address2',
            'town_or_city',
            'county',
            'country',
            'postcode',
        ]

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated labels
        """

        super().__init__(*args, **kwargs)

        placeholders = {
            'fname': 'First Name',
            'lname': 'Last Name',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'town_or_city': 'Town or City',
            'county': 'County',
            'postcode': 'Postal Code',
        }

        self.fields['fname'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
            self.fields[field].widget.attrs['class'] = 'form form-control mt-3'


        
  