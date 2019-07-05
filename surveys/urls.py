"""surveys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.urls import path
from django.views.generic import TemplateView

from devs import views as devs_views
from general import views as general_views

urlpatterns = [
    path('%s/' % settings.ADMIN_URL, admin.site.urls),
    path(
        '',
        TemplateView.as_view(template_name='landing.html'),
        name='landing'
    ),
    path('dev-survey/', devs_views.dev_survey, name='dev-survey'),
    path('user-survey/', general_views.user_survey, name='user-survey'),
    path(
        'privacy/',
        TemplateView.as_view(template_name='privacy.html'),
        name='privacy'
    ),
    path('success-dev/', devs_views.success_dev, name='success-dev'),
    path('success-user/', general_views.success_user, name='success-user'),
]
