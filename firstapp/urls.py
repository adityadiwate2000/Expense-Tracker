# firstapp/urls.py (app-level)

from django.urls import path
from . import views  # Import views from current directory

urlpatterns = [
    path('login/', views.login_view, name='login'),  # Login URL
    path('result/', views.result, name='result'),
    path('add-expense/', views.add_expense_view, name='add_expense'),  # Add expense URL
    path('expense-list/', views.expense_list, name='expense_list'),  # Expense list URL
    path('', views.home, name='home'),  # Home page URL
    path('go',views.result)
]
