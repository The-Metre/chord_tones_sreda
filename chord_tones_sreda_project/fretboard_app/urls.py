from django.urls import path
from fretboard_app import views

urlpatterns = [
    path('', views.fretboard_index, name='fretboard_index'),
]
