
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from seeds.models import Seeds

class SeedsListView(ListView):
    model = Seeds
    template_name = "seeds/seeds_list.html"


class SeedsDetailView(DetailView):
    model = Seeds
    template_name = "seeds/seeds_detail.html"
    fields = ['name', 'price', 'description']


class SeedsCreateView(LoginRequiredMixin, CreateView):
    model = Seeds
    success_url = reverse_lazy('seeds:seeds-list')
    fields = ['name', 'price', 'description']


class SeedsUpdateView(LoginRequiredMixin, UpdateView):
    model = Seeds
    success_url = reverse_lazy('seeds:seeds-list')
    fields = ['name', 'price', 'description']


class SeedsDeleteView(LoginRequiredMixin, DeleteView):
    model = Seeds
    success_url = reverse_lazy('seeds:seeds-list')

