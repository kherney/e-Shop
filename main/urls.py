"""e_shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from django.views.generic import TemplateView
from main import views

urlpatterns = [
    path('', TemplateView.as_view(template_name="home.html"), name="home"),
    path('about_us/', TemplateView.as_view(template_name="about_us.html"), name="about_us"),
    # path("contact_us/", views.contact_us, name="contact_us")
    path('contact_us/', views.ContactUsView.as_view(), name="contact_us"),
]