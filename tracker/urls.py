from django.urls import path
from . import views
from django.urls import include, path
from rest_framework import routers


app_name = 'tracker'  

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'category', views.CategoryViewSet)
router.register(r'expense', views.ExpenseViewSet)
router.register(r'income', views.IncomeViewSet)

urlpatterns = [
   path('', views.IndexView.as_view(), name='index'),

   path('api/', include(router.urls)),
   path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]