from django import forms
from .models import Message


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
