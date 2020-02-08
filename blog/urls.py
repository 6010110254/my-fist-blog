from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('contact/', views.contact, name='contact'),
    path('aboutme/', views.aboutme, name='aboutme'),
]