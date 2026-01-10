from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render, redirect
from django.views import View

from .forms import BoxCreateForm
from .models import Card, Box
from .owner import OwnerDeleteView, OwnerListView
from django.urls import reverse_lazy

class MainView(OwnerListView):
    model = Box

class DetailView(LoginRequiredMixin, View):
    model = Card
    template_name = 'cards/card_detail.html'

    def get(self, request, pk):
        x = get_object_or_404(Card,box=pk)
        context = {'question': x.name, 'answer': x.answer}
        return render(request, self.template_name, context)


class BoxCreateView(LoginRequiredMixin, View):
    model = Box
    fields = ['name', 'capacity', 'state']
    template_name = 'cards/box_form.html'
    success_url = reverse_lazy('cards:all')

    def get(self, request):
        form = BoxCreateForm()
        ctx = {'form': form}
        return render(request, self.template_name, ctx)

    def post(self, request):
        form = BoxCreateForm(request.POST)
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template_name, ctx)

        box = form.save(commit=False)
        box.owner = request.user
        box.save()
        return redirect(self.success_url)


class BoxUpdateView(LoginRequiredMixin, View):
    model = Box
    fields = ['name', 'capacity', 'state']
    template_name = 'cards/box_form.html'
    success_url = reverse_lazy('cards:all')

    def get(self, request, pk):
        box = get_object_or_404(Box, box=pk, owner=self.request.user)
        form = BoxCreateForm(instance=box)
        ctx = {'form': form}
        return render(request, self.template_name, ctx)

    def post(self, request, pk=None):
        box = get_object_or_404(Box, box=pk, owner=self.request.user)
        form = BoxCreateForm(request.POST, instance=box)
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template_name, ctx)

        form.owner = request.user
        form.save()
        return redirect(self.success_url)


class BoxDeleteView(OwnerDeleteView):
    model = Box
    field = '__all__'
    success_url = reverse_lazy('cards:all')