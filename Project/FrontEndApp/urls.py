from django.urls import path
from .views import *

urlpatterns=[
    path('home/',homeview,name='home'),
    path('info/',infoview,name='info'),
    path('addStudent/',addStudent,name='addStudent'),

]