from django.urls import path, include
from members.views import *

urlpatterns = [
   path('login', login, name="login"),
]