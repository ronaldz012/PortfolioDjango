from django.contrib import admin
from django.urls import path
from . import views
app_name = 'core'
urlpatterns = [
    path('',views.test, name='test'),
    path('home/',views.home, name='home'),
    path("/projects", views.projects, name="projects"),
    path('about/',views.about, name='about'),
    path('contact/',views.contact, name='contact'),    
]
