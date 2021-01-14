from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Patient
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required

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


@login_required
def home(request):
    # create a dictionary called context.Create a key within the dictionary called post, value assigned will be posts dictionary.
    # Now we can pass context to the render function and pass data into our template to use.
    context = {
        'patients': data
    }
    return render(request, 'core/home.html', context)


def landingpage(request):
    return render(request, 'core/landingpage.html')
# Class based view


class PatientListView(LoginRequiredMixin, ListView):
    model = Patient
    template_name = 'core/home.html'
    # <app>/<model>_<viewtype>.html
    context_object_name = 'patients'
    ordering = ['PatientID']


class PatientDetailView(DetailView):
    model = Patient

# View with a form to create a patient

# LoginRequiredMixin redirects not logged in user to login to add a new form


class PatientCreateView(LoginRequiredMixin, CreateView):
    model = Patient
    fields = ['PatientID', 'PatientSSN', 'FirstName',
              'LastName', 'Address', 'DOB', 'Sex', 'Author']

    def form_valid(self, form):
        # Take instance and set author = to current logged in user
        form.instance.author = self.request.user
        return super().form_valid(form)


class PatientUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Patient
    fields = ['PatientID', 'PatientSSN', 'FirstName',
              'LastName', 'Address', 'DOB', 'Sex', 'Author']

    def form_valid(self, form):
        # Take instance and set author = to current logged in user
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        # get object, Prevent other users from updating other patients info not created by the original creator
        patient = self.get_object()
        if self.request.user == patient.Author:
            return True
        return False

# Require a user logged in and Author of view


class PatientDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Patient
    success_url = '/'

    def test_func(self):
        # get object, Prevent other users from updating other patients info.
        patient = self.get_object()
        if self.request.user == patient.Author:
            return True
        return False


def about(request):
    return render(request, 'core/about.html', {'Title': 'About'})
