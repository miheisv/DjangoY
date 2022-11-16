import datetime
import random

from django.shortcuts import render

from catalog.models import Item


def home(request):
    template_name = 'homepage/homepage.html'
    items = Item.objects.published_home()
    context = {
        'items': items,
    }
    return render(request, template_name, context)
