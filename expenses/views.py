from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Expense

# Create your views here.
class IndexView(TemplateView):
    template_name = 'expenses/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['expenses'] = Expense.objects.all()
        return context