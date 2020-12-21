from django.shortcuts import render

# Create your views here.

# Return a render template instead of httpresponse
# Takes request as first argument, second is the template name. Third optional argument is context


def home(request):
    return render(request, 'core/home.html')


def about(request):
    return render(request, 'core/about.html')
