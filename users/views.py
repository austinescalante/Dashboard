from django.shortcuts import render, redirect
from django.contrib import messages
# Add this from forms.py instead of UserCreationForm
from . forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
# For Profile view
from django.contrib.auth.decorators import login_required

# Create a register view


def register(request):
    if request.method == 'POST':
        # Create a new form that has data within the POST
        form = UserRegisterForm(request.POST)
        # Is the form valid, if not moves to the else condition
        if form.is_valid():
            # Saving the user, hash the password and will show up in the admin panel
            form.save()
            username = form.cleaned_data.get('username')
            # Flash message and redirect user to home page
            messages.success(
                request, f'Your Account has been created! You will be able to login')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

# Decorator for function, user must be logged in to view the profile. Profile path will not redirect user until the user has log in status


@login_required
def Profile(request):
    # Check if post route and for form validity
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        # Check if both are valid
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            # Feedback to user
            messages.success(
                request, f'Your Account has been updated')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    # Pass into template, have keys we access in the template
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    # Require a user is logged in to look at view
    return render(request, 'users/profile.html', context)
