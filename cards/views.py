from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Card


class MainView(ListView):
    template_name = 'cards/index.html'
    model = Card

class CreateView(CreateView):