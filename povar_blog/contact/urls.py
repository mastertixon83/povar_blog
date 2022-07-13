from django.urls import path
from .views import *

app_name = 'contact'

urlpatterns = [
    path('contact/', ContactView.as_view(), name='contact'),
    path('feedback/', CreateContact.as_view(), name='feedback'),
]