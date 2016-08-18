from django.shortcuts import render, redirect

from django.views import generic
from .form import ContactForm


class HomePage(generic.TemplateView):
    template_name = "home.html"


class AboutPage(generic.TemplateView):
    template_name = "about.html"


def contact(request):
    form_class = ContactForm
    return render(request, 'contact.html', {'form': form_class})



class NosOffresPage(generic.TemplateView):
    template_name = "nos-offres.html"
