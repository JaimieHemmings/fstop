from django import forms
from .models import (
  ServicesHero,
  ServicesBanner,
  ServicesCards,
  ServicesContextBannerOne,
  ServicesContextBannerTwo,
)


class ServicesHeroForm(forms.ModelForm):
    class Meta:
        model = ServicesHero
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'title': 'Enter the title of the hero image',
            'lead': 'Enter the lead text for the hero image',
            'alt_text': 'Enter the alt text for the hero image',
        }
        
        # Set autofocus on first field to be filled in
        self.fields['title'].widget.attrs['autofocus'] = True
        
        for field in self.fields:
            if field != 'image':
              # Add classes to each field
              self.fields[field].widget.attrs['class'] = 'form form-control mt-1 mb-3'
              # Add placeholders
              self.fields[field].widget.attrs['placeholder'] = placeholders[field]


class ServicesBannerForm(forms.ModelForm):
    class Meta:
        model = ServicesBanner
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'title': 'Enter the title of the banner image',
            'lead': 'Enter the lead text for the banner image',
            'alt_text': 'Enter the alt text for the banner image',
        }
        
        # Set autofocus on first field to be filled in
        self.fields['title'].widget.attrs['autofocus'] = True
        
        for field in self.fields:
            if field != 'image':
              # Add classes to each field
              self.fields[field].widget.attrs['class'] = 'form form-control mt-1 mb-3'
              # Add placeholders
              self.fields[field].widget.attrs['placeholder'] = placeholders[field]


class ServicesCardsForm(forms.ModelForm):
    class Meta:
        model = ServicesCards
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'title': 'Enter the title of the card',
            'lead': 'Enter the lead text for the card',
            'icon': 'Enter the alt text for the card',
        }
        
        # Set autofocus on first field to be filled in
        self.fields['title'].widget.attrs['autofocus'] = True
        
        for field in self.fields:
            if field != 'image':
              # Add classes to each field
              self.fields[field].widget.attrs['class'] = 'form form-control mt-1 mb-3'
              # Add placeholders
              self.fields[field].widget.attrs['placeholder'] = placeholders[field]