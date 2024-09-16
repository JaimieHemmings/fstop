from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages

def index(request):
    """
    A view that displays the index page
    """
    return render(request, 'home/index.html')

def about(request):
    """
    A view that displays the about page
    """
    return render(request, 'home/about.html')

def contact(request):
    """
    A view that displays the contact page
    """
    context = {}
    form = ContactForm()
    context['form'] = form

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # Flash Message confirmation
            messages.success(request, 'Your message has been sent!')
            # Redirect to Contact page            
            return redirect('/contact')
        else:
            # Flash Message error
            messages.error(request, 'Error sending message. Please check the form.')
            return redirect('/contact')

    return render(request, 'home/contact.html', context)
