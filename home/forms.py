from django import forms
from .models import Message, HomePageHero, HomePageAbout, HomePageTrustedBy, HomePageFAQs


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
            "cover_image": "",
        }

        helper_text = {
            "hero_title": "The title for the hero section",
            "hero_subtitle": "The subtitle for the hero section",
            "hero_list_one": "The first item in the hero list",
            "hero_list_two": "The second item in the hero list",
            "hero_list_three": "The third item in the hero list",
            "hero_list_four": "The fourth item in the hero list",
            "data_one_value": "The value for the first data point",
            "data_one_title": "The title for the first data point",
            "data_two_value": "The value for the second data point",
            "data_two_title": "The title for the second data point",
            "data_three_value": "The value for the third data point",
            "data_three_title": "The title for the third data point",
            "hero_image": "The background image for the hero section",
        }

        field_labels = {
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
            "hero_image": "Hero Image",
        }

        for field in self.fields:
            # Add helpertext to each field
            self.fields[field].help_text = helper_text[field]
            # Set autofocus on first field to be filled in
            if field == "hero_title":
                self.fields[field].widget.attrs["autofocus"] = True
            self.fields[field].widget.attrs["class"] = "form form-control mt-1"
            # Set field labels
            self.fields[field].label = field_labels[field]
            # Set placeholders
            if field != "hero_image":
                if self.fields[field].required:
                    placeholder = f"{placeholders[field]} *"
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs["placeholder"] = placeholder


class editAboutSectionHomeForm(forms.ModelForm):
    class Meta:
        model = HomePageAbout
        fields = [
            "homepage_about_title",
            "homepage_about_lead",
            "homepage_about_subtitle",
            "homepage_about_paragraph_one",
            "homepage_about_paragraph_two",
            "homepage_about_image",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            "homepage_about_title": "Enter the title of the about section",
            "homepage_about_lead": "Enter the lead of the about section",
            "homepage_about_subtitle": "Enter the subtitle of the about section",
            "homepage_about_paragraph_one": "Enter the first paragraph of the about section",
            "homepage_about_paragraph_two": "Enter the second paragraph of the about section",
        }

        # Set autofocus on first field to be filled in
        self.fields["homepage_about_title"].widget.attrs["autofocus"] = True

        for field in self.fields:
            if field != "homepage_about_image":
                # Add classes to each field
                self.fields[field].widget.attrs["class"] = "form form-control mt-1 mb-3"
                # Add placeholders
                self.fields[field].widget.attrs["placeholder"] = (
                    placeholders[field]
                )


class HomePageTrustedByForm(forms.ModelForm):
    class Meta:
        model = HomePageTrustedBy
        fields = [
            "trusted_by_title",
            "trusted_by_lead",
            "img_one",
            "img_two",
            "img_three",
            "img_four",
            "img_five",
            "img_six",
            "img_seven",
            "img_eight",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            "trusted_by_title": "Enter the title of the trusted by section",
            "trusted_by_lead": "Enter the lead of the trusted by section",
        }

        # Set autofocus on first field to be filled in
        self.fields["trusted_by_title"].widget.attrs["autofocus"] = True
        # set classes
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form form-control mt-1 mb-3"


class HomePageFAQsForm(forms.ModelForm):
    class Meta:
        model = HomePageFAQs
        fields = ["faq_question", "faq_answer"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            "faq_question": "Enter a question for the FAQ section",
            "faq_answer": "Enter an answer for the FAQ section",
        }



        # Set autofocus on first field to be filled in
        self.fields["faq_question"].widget.attrs["autofocus"] = True
        # set classes
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form form-control mt-1 mb-3"
            self.fields[field].widget.attrs["placeholder"] = placeholders[field]