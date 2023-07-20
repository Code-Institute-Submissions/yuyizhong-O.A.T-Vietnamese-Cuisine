from django.shortcuts import render

from django.views.generic import TemplateView


class ContactView(TemplateView):
    """
    View to render contact page
    """
    template_name = 'contact/contact.html'
