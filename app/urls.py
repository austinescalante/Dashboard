"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

# Core/-map core to core.urls then within empty path maps to home view. Sends remaining string to core.urls, send remaining after core/ so it sends an empty string
# to core.urls

# Match patterns in the urls.py in the other py file. Chops off core/ and passes anthing after to core.urls, checks for matches and then goes
# to the views function
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls'))
]
