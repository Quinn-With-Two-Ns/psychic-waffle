from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import TemplateView

# Create your views here.

class MainPageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'main.html', context=None)