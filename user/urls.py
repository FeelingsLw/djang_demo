from django.urls import path,include
from user.views import *

app_name ='user'
urlpatterns = [
    path('login/',login,name='login'),
    path('register/',RegisterView.as_view()),
    path('logout/',logout,name='logout'),
]