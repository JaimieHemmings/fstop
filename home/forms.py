from django import forms
from .models import Message, HomePageHero


class ContactForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ["fname", "lname", "email", "message"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            "fname": "First Name",
            "lname": "Last Name",
            "email": "Email Address",
            "message": "Message",
        }

        # Set minimum length values
        self.fields["fname"].widget.attrs["minlength"] = 2
        self.fields["lname"].widget.attrs["minlength"] = 3
        self.fields["message"].widget.attrs["minlength"] = 10
        # Set autofocus on first field to be filled in
        self.fields["fname"].widget.attrs["autofocus"] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f"{placeholders[field]} *"
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs["placeholder"] = placeholder
            self.fields[field].widget.attrs["class"] = "form form-control mt-3"
            self.fields[field].label = False


class HomeHeroForm(forms.ModelForm):
    class Meta:
        model = HomePageHero
        fields = [
            "hero_title",
            "hero_subtitle",
            "hero_image",
            "hero_list_one",
            "hero_list_two",
            "hero_list_three",
            "hero_list_four",
            "data_one_value",
            "data_one_title",
            "data_two_value",
            "data_two_title",
            "data_three_value",
            "data_three_title",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            "hero_title": "Hero Title",
            "hero_subtitle": "Hero Subtitle",
            "hero_list_one": "Hero List One",
            "hero_list_two": "Hero List Two",
            "hero_list_three": "Hero List Three",
            "hero_list_four": "Hero List Four",
            "data_one_value": "Data One Value",
            "data_one_title": "Data One Title",
            "data_two_value": "Data Two Value",
            "data_two_title": "Data Two Title",
            "data_three_value": "Data Three Value",
            "data_three_title": "Data Three Title",
        }

        for field in self.fields:
            # Set autofocus on first field to be filled in
            if field != "hero_image":
                if field == "hero_title":
                    self.fields[field].widget.attrs["autofocus"] = True
                if self.fields[field].required:
                    placeholder = f"{placeholders[field]} *"
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs["placeholder"] = placeholder
                self.fields[field].widget.attrs["class"] = "form form-control mt-3"
                self.fields[field].label = False