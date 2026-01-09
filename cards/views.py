from .models import Card
from .owner import OwnerDeleteView, OwnerListView, OwnerCreateView, \
    OwnerUpdateView, OwnerDetailView


class MainView(OwnerListView):
    model = Card

class DetailView(OwnerDetailView):
    model = Card

class CreateView(OwnerCreateView):
    model = Card
    fields = ['question', 'answer']

class UpdateView(OwnerUpdateView):
    model = Card
    fields = ['question', 'answer']

class DeleteView(OwnerDeleteView):
    model = Card