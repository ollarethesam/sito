from django.urls import path
from . import views

urlpatterns = [
    path('home', views.index, name='home'),
    path('contact', views.contact, name='contact'),
    path('messaggio inviato', views.success_view, name='success'),
]