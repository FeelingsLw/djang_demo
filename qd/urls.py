from django.urls import path,include
from .views import *

app_name='qd'
urlpatterns = [
    path('index/',QdView.as_view()),
    path('list/',QdList.as_view(),name='list'),
]
