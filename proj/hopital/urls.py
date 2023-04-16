from django.urls import  path
from .views import *

urlpatterns = [
    path('patient/', patient_list,name='patient_list'),
    path('create/', create_patient ,name='create_patient')
]