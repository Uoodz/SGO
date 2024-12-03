from django.shortcuts import render
from django.urls import path

from .views import IndexView, TesteView, AjudaView, SobreView, solicitar_ajuda
from rest_framework.routers import SimpleRouter


router = SimpleRouter()

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('teste', TesteView.as_view(), name='teste'),
    path('sobre', SobreView.as_view(), name='sobre'),
    path('ajuda', AjudaView.as_view(), name='ajuda'),
    path('ajuda/', solicitar_ajuda, name='solicitar_ajuda'),
]
