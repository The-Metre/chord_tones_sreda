from django.urls import path
from chord_tones_app import views

urlpatterns = [
    path('', views.index, name='index'),
]
