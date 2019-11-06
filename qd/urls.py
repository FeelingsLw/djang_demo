from django.urls import path,include
from .views import *

urlpatterns = [
    path('index/',QdView.as_view()),
    path('list/',QdList.as_view()),
]
