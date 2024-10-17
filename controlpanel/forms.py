from django import forms
from blog.models import Article
from portfolio.models import PortfolioImages
from reviews.models import Review
from payments.models import Payment


class CreateArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            "title",
            "exerpt",
            "thumb",
            "slider_image_one",
            "slider_image_two",
            "slider_image_three",
            "slider_image_four",
            "body",
            "body_image",
            "body_continued",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            "title": "Enter the title of the article",
            "exerpt": "Emter a small exerpt of the article",
            "body": "Enter the article content before the image break",
            "body_continued": "Enter the remaining content of the article",
        }

        # Set autofocus on first field to be filled in
        self.fields["title"].widget.attrs["autofocus"] = True

        # Create helper text for each field
        help_text = {
            "title": "Enter the title of the article",
            "exerpt": "Enter the exerpt of the article",
            "body": "Enter the article content before the image break",
            "body_continued": "Enter the remaining content of the article",
            "thumb": "Enter the thumbnail image for the article",
            "slider_image_one": "Enter the cover image for the article, "
            "this image will also be displayed in the gallery within the body"
            " of the article",
            "slider_image_two": "The second image used in the gallery within "
            "the body of the article",
            "slider_image_three": "The third image used in the gallery of the"
            " article",
            "slider_image_four": "The fourth item used in the gallery",
            "body_image": "Enter the body image for the article, displayed "
            "in the middle of the article",
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
                and field != "body_image"
                and field != "slider_image_one"
                and field != "slider_image_two"
                and field != "slider_image_three"
                and field != "slider_image_four"
            ):
                # Add placeholders
                self.fields[field].widget.attrs["placeholder"] = (
                    placeholders[field]
                )


class AddPortfolioImage(forms.ModelForm):
    class Meta:
        model = PortfolioImages
        fields = ["title", "image", "description"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            "title": "Enter the title of the image",
            "description": "Enter a description of the image",
        }

        # Set autofocus on first field to be filled in
        self.fields["title"].widget.attrs["autofocus"] = True

        for field in self.fields:
            # Add classes to each field
            self.fields[field].widget.attrs["class"] = (
                "form form-control mt-1 mb-3"
                )
            # Add placeholders if not the image fields
            if field != "image":
                self.fields[field].widget.attrs["placeholder"] = (
                    placeholders[field]
                    )


class AddReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["name", "company", "content", "user_img"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            "name": "Enter the name of the reviewer",
            "company": "Enter the company of the reviewer",
            "content": "Enter the review content",
        }

        # Set autofocus on first field to be filled in
        self.fields["name"].widget.attrs["autofocus"] = True

        for field in self.fields:
            # Add classes to each field
            self.fields[field].widget.attrs["class"] = (
                "form form-control mt-1 mb-3"
                )
            # Add placeholders if not the image fields
            if field != "user_img":
                self.fields[field].widget.attrs["placeholder"] = (
                    placeholders[field]
                    )


class NewPaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ["email", "amount", "description"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            "email": "Enter the payees email address",
            "amount": "Enter the payment amount",
            "description": "Enter a description of the Services",
        }

        # Set autofocus on first field to be filled in
        self.fields["email"].widget.attrs["autofocus"] = True

        for field in self.fields:
            # Add classes to each field
            self.fields[field].widget.attrs["class"] = (
                "form form-control mt-1 mb-3"
                )
            # Add placeholders if not the image fields
            self.fields[field].widget.attrs["placeholder"] = (
                placeholders[field]
                )
