from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def fretboard_index(request):
    return render(request, 'fretboard.html')

