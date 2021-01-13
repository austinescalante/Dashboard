from django.urls import path
from . import views
from . views import PatientListView, PatientDetailView, PatientCreateView, PatientUpdateView, PatientDeleteView

# empty path,specify view to handle logic(views.screen), an a name for the path.
# Receives a empty string, it matches with the '' and goes to the views home function.
# Then goes through the function
urlpatterns = [

    #path('', views.home, name='home'),
    # Class based view
    path('home/', PatientListView.as_view(), name='home'),
    path('', views.landingpage, name='landingpage'),
    path('about/', views.about, name='about'),
    # url pattern with variable, to have DV grab an object
    path('patient/<int:pk>/', PatientDetailView.as_view(), name='patient-detail'),
    path('patient/new/', PatientCreateView.as_view(), name='patient-create'),
    path('patient/<int:pk>/update/',
         PatientUpdateView.as_view(), name='patient-update'),
    path('patient/<int:pk>/delete/',
         PatientDeleteView.as_view(), name='patient-delete')


]
# <app>/<model>_<viewtype>.html
