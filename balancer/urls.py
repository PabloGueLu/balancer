from django.urls import path
from . import views

urlpatterns = [
    path('', views.panel_board, name = 'panel_board'),
]