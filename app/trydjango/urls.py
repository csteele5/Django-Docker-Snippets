"""trydjango URL Configuration

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
from django.contrib import admin
from django.urls import path, include
"""  this was the original way of doing this and it worked
from pages import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('contact/', views.contact_view, name='contact'),
    path('admin/', admin.site.urls),
]
"""

#this imports specific views from the pages application - either way, the views should be uniquely nameed
from pages.views import home_view, contact_view, about_view

urlpatterns = [
    path('classview/', include('classviewtest.urls')),
    path('viewtest/', include('viewtest.urls')),
    path('courses/', include('courses.urls')),
    path('articlesnew/', include('blognew.urls')),
    path('articles/', include('blog.urls')),
    path('products/', include('products.urls')),
    path('', home_view, name='home'),
    path('contact/', contact_view, name='contact'),
    path('about/', about_view, name='about'),
    path('admin/', admin.site.urls),
]
