from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add-contact/', views.add_contact, name='add-contact'),
    path('profile/<id:pk>/', views.contact_profile, name='contact-profile'),
]