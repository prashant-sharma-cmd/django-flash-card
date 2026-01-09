from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

class OwnerListView(ListView):
    pass

class OwnerDetailView(DetailView):
    pass

class OwnerCreateView(LoginRequiredMixin, CreateView):
    pass

class OwnerUpdateView(LoginRequiredMixin, UpdateView):
    pass

class OwnerDeleteView(LoginRequiredMixin, DeleteView):
    pass
