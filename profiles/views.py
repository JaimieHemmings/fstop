from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from payments.models import Payment


@login_required
def profile(request):
    """
    View to display the user's profile
    """
    user = request.user
    # Get all payment requests matching the users email address
    payments = Payment.objects.filter(email=user.email)

    context = {
        'user': user,
        'payments': payments,
    }
    
    return render(request, 'profile.html', context)






