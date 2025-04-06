from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Expense, Income, Category
from django.http import HttpResponse

from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets

from .serializers import GroupSerializer, UserSerializer, CategorySerializer, ExpenseSerializer, IncomeSerializer

# Create your views here.
class IndexView(ListView):
    #model = Expense
    queryset = Expense.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['expenses'] = Expense.objects.all()
        context['incomes'] = Income.objects.all()
        context['categorys'] = Category.objects.all()
        return context

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class CategoryViewSet (viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer

class ExpenseViewSet (viewsets.ModelViewSet):
    queryset = Expense.objects.all().order_by('date')
    serializer_class = ExpenseSerializer

class IncomeViewSet (viewsets.ModelViewSet):
    queryset = Income.objects.all().order_by('date')
    serializer_class = IncomeSerializer