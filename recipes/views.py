from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# HTTP REQUEST
def home(request):
    # HTTP RESPONSE
    return render(request, 'recipes/pages/home.html')

