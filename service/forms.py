from .models import ServicesPage
from django import forms

class EditServicesPageForm(forms.ModelForm):
    class Meta:
        model = ServicesPage
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            "title": "Enter the title of the page",
            "hero_title": "Enter the title of the hero section",
            "hero_image": "Upload the hero image",
            "list_item_one": "Enter the first list item",
            "list_item_two": "Enter the second list item",
            "list_item_three": "Enter the third list item",
            "list_item_four": "Enter the fourth list item",
            "banner_image": "Upload the banner image",
            "banner_alt_text": "Enter the alt text for the banner image",
            "highlight_one_title": "Enter the title for the first highlight",
            "highlight_one_lead": "Enter the lead for the first highlight",
            "highlight_one_image": "Upload the image for the first highlight",
            "highlight_one_alt_text": "Enter the alt text for the first highlight image",
            "highlight_two_title": "Enter the title for the second highlight",
            "highlight_two_lead": "Enter the lead for the second highlight",
            "highlight_two_image": "Upload the image for the second highlight",
            "highlight_two_alt_text": "Enter the alt text for the second highlight image",
            "service_info_one_title": "Enter the title for the first service info",
            "service_info_one_lead": "Enter the lead for the first service info",
            "service_info_one_image": "Upload the image for the first service info",
            "service_info_one_alt_text": "Enter the alt text for the first service info image",
            "service_info_two_title": "Enter the title for the second service info",
            "service_info_two_lead": "Enter the lead for the second service info",
            "service_info_two_image": "Upload the image for the second service info",
            "service_info_two_alt_text": "Enter the alt text for the second service info image",
        }

        # Set autofocus on first field to be filled in
        self.fields["title"].widget.attrs["autofocus"] = True

        # Create helper text for each field
        help_text = {
            "title": "Enter the title of the page",
            "hero_title": "Enter the title of the hero section",
            "hero_image": "Upload the hero image",
            "list_item_one": "Enter the first list item",
            "list_item_two": "Enter the second list item",
            "list_item_three": "Enter the third list item",
            "list_item_four": "Enter the fourth list item",
            "banner_image": "Upload the banner image",
            "banner_alt_text": "Enter the alt text for the banner image",
            "highlight_one_title": "Enter the title for the first highlight",
            "highlight_one_lead": "Enter the lead for the first highlight",
            "highlight_one_image": "Upload the image for the first highlight",
            "highlight_one_alt_text": "Enter the alt text for the first highlight image",
            "highlight_two_title": "Enter the title for the second highlight",
            "highlight_two_lead": "Enter the lead for the second highlight",
            "highlight_two_image": "Upload the image for the second highlight",
            "highlight_two_alt_text": "Enter the alt text for the second highlight image",
            "service_info_one_title": "Enter the title for the first service info",
            "service_info_one_lead": "Enter the lead for the first service info",
            "service_info_one_image": "Upload the image for the first service info",
            "service_info_one_alt_text": "Enter the alt text for the first service info image",
            "service_info_two_title": "Enter the title for the second service info",
            "service_info_two_lead": "Enter the lead for the second service info",
            "service_info_two_image": "Upload the image for the second service info",
            "service_info_two_alt_text": "Enter the alt text for the second service info image",
        }

        for field in self.fields:
            # Add classes to each field
            self.fields[field].widget.attrs["class"] = "form form-control mt-2"
            # Add help text to each field after the field
            self.fields[field].help_text = help_text[field]
            # Add classes to the help text
            self.fields[field].help_text = f"<small>{help_text[field]}</small>"
            # If field type is not an image
            if (
                field != "thumb"
                and field != "hero_image"
                and field != "banner_image"
                and field != "highlight_one_image"
                and field != "highlight_two_image"
                and field != "service_info_one_image"
                and field != "service_info_two_image"
            ):
                # Add placeholders
                self.fields[field].widget.attrs["placeholder"] = (
                    placeholders[field]
                )