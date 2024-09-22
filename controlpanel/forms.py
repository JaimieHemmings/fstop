from django import forms
from blog.models import Article
from portfolio.models import SliderImages, PortfolioImages
from reviews.models import Review

class CreateArticleForm(forms.ModelForm):
  class Meta:
        model = Article
        fields = [
            'title',
            'exerpt',
            'thumb',
            'slider_image_one',
            'slider_image_two',
            'slider_image_three',
            'slider_image_four',
            'body',
            'body_image',
            'body_continued'
            ]

  def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'title': 'Enter the title of the article',
            'exerpt': 'Emter a small exerpt of the article',
            'body': 'Enter the article content before the image break',
            'body_continued': 'Enter the remaining content of the article',
        }

        # Set autofocus on first field to be filled in
        self.fields['title'].widget.attrs['autofocus'] = True

        # Create helper text for each field
        help_text = {
            'title': 'Enter the title of the article',
            'exerpt': 'Enter the exerpt of the article',
            'body': 'Enter the article content before the image break',
            'body_continued': 'Enter the remaining content of the article',
            'thumb': 'Enter the thumbnail image for the article',
            'slider_image_one': 'Enter the cover image for the article',
            'slider_image_two': 'Enter the cover image for the article',
            'slider_image_three': 'Enter the cover image for the article',
            'slider_image_four': 'Enter the cover image for the article',            
            'body_image': 'Enter the body image for the article',
        }

        for field in self.fields:
            # Add classes to each field
            self.fields[field].widget.attrs['class'] = 'form form-control mt-2'
            # Add help text to each field after the field
            self.fields[field].help_text = help_text[field]
            # Add classes to the help text
            self.fields[field].help_text = f'<small>{help_text[field]}</small>'
            # If field is not image type
            if field != 'thumb' and field != 'slider_image_one' and field != 'slider_image_two' and field != 'slider_image_three' and field != 'slider_image_four' and field != 'body_image':
                self.fields[field].widget.attrs['placeholder'] = placeholders[field]


class AddSliderImage(forms.ModelForm):
    class Meta:
        model = SliderImages
        fields = ['title', 'image', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'title': 'Enter the title of the image',
            'description': 'Enter a description of the image',
        }

        # Set autofocus on first field to be filled in
        self.fields['title'].widget.attrs['autofocus'] = True

        for field in self.fields:
            # Add classes to each field
            self.fields[field].widget.attrs['class'] = 'form form-control mt-1 mb-3'
            # Add placeholders if not the image fields
            if field != 'image':
                self.fields[field].widget.attrs['placeholder'] = placeholders[field]


class AddPortfolioImage(forms.ModelForm):
    class Meta:
        model = PortfolioImages
        fields = ['title', 'image', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'title': 'Enter the title of the image',
            'description': 'Enter a description of the image',
        }

        # Set autofocus on first field to be filled in
        self.fields['title'].widget.attrs['autofocus'] = True

        for field in self.fields:
            # Add classes to each field
            self.fields[field].widget.attrs['class'] = 'form form-control mt-1 mb-3'
            # Add placeholders if not the image fields
            if field != 'image':
                self.fields[field].widget.attrs['placeholder'] = placeholders[field]


class AddReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'company', 'content', 'user_img']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Enter the name of the reviewer',
            'company': 'Enter the company of the reviewer',
            'content': 'Enter the review content',
        }

        # Set autofocus on first field to be filled in
        self.fields['name'].widget.attrs['autofocus'] = True

        for field in self.fields:
            # Add classes to each field
            self.fields[field].widget.attrs['class'] = 'form form-control mt-1 mb-3'
            # Add placeholders if not the image fields
            if field != 'user_img':
                self.fields[field].widget.attrs['placeholder'] = placeholders[field]

