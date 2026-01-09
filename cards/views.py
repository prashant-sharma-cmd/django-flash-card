from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.views import View

from .models import Card
from .owner import OwnerDeleteView, OwnerListView, OwnerCreateView, \
    OwnerUpdateView, OwnerDetailView
from django.urls import reverse, reverse_lazy

class MainView(OwnerListView):
    model = Card

class DetailView(LoginRequiredMixin, View):
    model = Card
    template_name = 'cards/card_detail.html'

    def get(self, request, pk):
        x = get_object_or_404(Card, pk=pk)
        context = {'question': x.question, 'answer': x.answer}
        return render(request, self.template_name, context)


class CreateView(OwnerCreateView):
    model = Card
    fields = ['question', 'answer']
    success_url = reverse_lazy('cards:all')

class UpdateView(OwnerUpdateView):
    model = Card
    fields = ['question', 'answer']
    success_url = reverse_lazy('cards:all')


class DeleteView(OwnerDeleteView):
    model = Card
    field = '__all__'
    success_url = reverse_lazy('cards:all')