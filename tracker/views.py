from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Expense
from django.http import HttpResponse

# Create your views here.
class IndexView(ListView):
    model = Expense
    queryset = Expense.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['expenses'] = Expense.objects.all()
        return context