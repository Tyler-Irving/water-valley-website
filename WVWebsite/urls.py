"""WVWebsite URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from WVWebsite.app.views import render_page, new_post
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", render_page, name="Home"),
    url(r"^tinymce/", include("tinymce.urls")),
    path("accounts/", include("allauth.urls")),
    path("index", TemplateView.as_view(template_name="index2.html")),
    path("new_post", new_post, name="new_post"),
]
