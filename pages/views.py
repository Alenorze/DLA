from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import View, FormView, CreateView, DetailView

from newsletter.forms import JoinForm
from .models import Page


class HomeView(SuccessMessageMixin, CreateView):
    template_name = 'pages/home.html'
    form_class = JoinForm
    success_url = '/'

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['object'] = Page.objects.filter(featured=True).first()
        return context 

    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "Thank you!"


class PageDetailView(DetailView):
    queryset = Page.objects.filter(active=True)
    model = Page
    template_name = 'pages/home.html'