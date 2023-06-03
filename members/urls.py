from django.urls import path, include
from members.views import *

urlpatterns = [
   path('login', login, name="login"),
   path('logout', logout_user, name='logout'),
   path('register_user', register_user, name='register_user'),
]