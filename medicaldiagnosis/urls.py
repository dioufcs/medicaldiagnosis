"""medicaldiagnosis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.views.generic.base import TemplateView
from django.conf.urls.static import static
from search.views import synthetiseur, instantSearch
from dashboard.views import detailMaladie


urlpatterns = [

    #Section CSD
    path('dashboard/', include('dashboard.urls')),
    #Fin section CSD

	path('home', views.home_view, name='home'),
    path('admin/', admin.site.urls),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name="logout"),
    path('reset/', views.reset_password_view, name="reset"),
    path('password_change/', views.password_change_view, name="password_change"),
    path('ajax/synthetiseur/', synthetiseur, name='synthetiseur'),
    path('ajax/instantsearch/', instantSearch, name='instantSearch'),
    path('ajax/detailMaladie/', detailMaladie, name='detailMaladie'),
    
]