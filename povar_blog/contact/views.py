from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView

from .forms import ContactForm
from .models import *


class ContactView(View):
    def get(self, request):
        contacts = ContactLink.objects.all()
        form = ContactForm()
        return render(request, 'contact/contact.html', {'contacts': contacts, 'form': form})


class CreateContact(CreateView):
    """Форма добавления контактов"""
    form_class = ContactForm
    success_url = '/'


class AboutView(View):
    def get(self, request):
        about = About.objects.last()
        return render(request, 'contact/about.html', {'about': about})

