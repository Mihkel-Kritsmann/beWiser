from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Expense
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Welcome to the home page!")

class IndexView(ListView):
    model = Expense
    context_object_name = "expense_list"
    queryset = Expense.objects.all()
    template_name = "expenses/index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['expenses'] = Expense.objects.all()
        return context

class ExpenseDetailView(DetailView):
    model = Expense
    context_object_name = "expense_list"
    queryset = Expense.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['expenses'] = Expense.objects.all()
        return context