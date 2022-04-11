from django.shortcuts import render
from .models import Category, Smartphone

def home_view(request):
    categories = Category.objects.all().order_by('id')
    smartphones = Smartphone.objects.all().order_by('id')
    context = {
    'categories' : categories,
    'smartphones' : smartphones
    }
    return render(request, 'index.html', context)


def phone_view(request):
    context = {
    'salom' : "Assalomu alaykum"
    }
    return render(request, 'pages/catalog/phone.html', context)