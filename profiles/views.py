from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from payments.models import Payment
from .forms import UserProfileForm
from .models import UserProfile


@login_required
def profile(request):
    """
    View to display the user's profile
    """
    user = request.user
    user_profile = UserProfile.objects.get(user=user)
    payments = Payment.objects.filter(email=user.email)
    context = {
        'user': user,
        'payments': payments,
        'user_profile': user_profile
    }
    return render(request, 'profile.html', context)


@login_required
def edit_profile(request):
    """
    View to edit the user's profile
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    form = UserProfileForm(instance=profile)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return render(request, 'profile.html', {'user': request.user})
        else:
            form = UserProfileForm(instance=profile)
    context = {
        'form': form,
    }
    return render(request, 'edit-profile.html', context)
