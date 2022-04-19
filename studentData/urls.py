from django.urls import path
from . import views

urlpatterns = [
     path('', views.getDetails, name='certi_data'),
     path('generate_certificate', views.generate_certificate, name='certiGenerate')
]
