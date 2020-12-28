from django.shortcuts import render, redirect
from django.contrib import messages
# Add this from forms.py instead of UserCreationForm
from . forms import UserRegisterForm

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
            # Flash message and redirect user
            messages.success(request, f'Account created for {username}!')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
