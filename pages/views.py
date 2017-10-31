from django.shortcuts import render
from django.contrib.message.views import SuccessMessageMixin
from django.views.generic import View, FormView, CreateView

from newsletter.forms import JoinForm


class HomeView(CreateView):
    template_name = 'pages/home.html'
    form_class = JoinForm
    success_url = '/'

    def get_success_message(self, cleaned_data):
        return "Thank you!"

    # def form_valid(self, form):
    #     email = form.cleaned_data.get("email")
    #     return super(HomeView, self).form_valid(form)