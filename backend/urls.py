"""
URL configuration for bewiser project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
<<<<<<< HEAD:backend/urls.py
=======
#from expenses import views
>>>>>>> 89998ca66e22e929210207938c3ce1d06223e22f:bewiser/urls.py
from tracker import views


urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD:backend/urls.py
=======
    #path('expenses/', include('expenses.urls')),
>>>>>>> 89998ca66e22e929210207938c3ce1d06223e22f:bewiser/urls.py
    path('', include('tracker.urls')),
]