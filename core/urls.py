from django.urls import path
from . import views

# empty path,specify view to handle logic(views.screen), an a name for the path.
# Receives a empty string, it matches with the '' and goes to the views home function.
# Then goes through the function
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about')
]
