from django.shortcuts import render
from .models import Patient

# Create your views here.

# Return a render template instead of httpresponse
# Takes request as first argument, second is the template name. Third optional argument is context

# Dictionary
'''
posts = [
    {
        'Name': 'Jake',
        'EmployeeID': '3452',
        'Title': 'Doctor',
        'Date_Hired': 'June 6, 2020'
    },
    {
        'Name': 'Amy',
        'EmployeeID': '5231',
        'Title': 'Lawyer',
        'Date_Hired': 'April 24, 2020'
    }
]
'''

data = Patient.objects.all()


def home(request):
    # create a dictionary called context.Create a key within the dictionary called post, value assigned will be posts dictionary.
    # Now we can pass context to the render function and pass data into our template to use.
    context = {
        'patients': data
    }
    return render(request, 'core/home.html', context)


def about(request):
    return render(request, 'core/about.html', {'Title': 'About'})
