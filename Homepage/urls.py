from django.urls import path
from Homepage.views import *

app_name = 'homepage'

urlpatterns = [
    path('', HomePage1, name='homepage_1'),
    path('homepage2/', HomePage2, name='homepage_2'),
]