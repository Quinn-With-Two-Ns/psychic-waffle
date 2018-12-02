from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *
from .forms import NameForm
# Create your views here.

def post(self, request):
    form = NameForm(request.POST)
    template = 'login.html'
    if form.is_valid():
        text = form.cleaned_data['name']

    return render(request, template, {'form': form, 'text' : text})


def index(request):
    template = loader.get_template('main.html')
    all_ingredient = Ingredient.objects.all()
    context = {
        'all_ingredient' : all_ingredient,
    }
    return HttpResponse(template.render(context, request))

def login(request):
    template = 'login.html'
    form = NameForm()
    context = {
    }
    return render(request, template, {'form' : form})