from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def panel_board(request):
    return render(request, 'balancer/panel.html', {})