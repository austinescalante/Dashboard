# Register models to show up in admin page
from django.contrib import admin
from . models import Patient

admin.site.register(Patient)
