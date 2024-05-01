# firstapp/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.db import connection
from .models import Expense
import mysql.connector
from .forms import ExpenseForm
from django.db.utils import OperationalError  # Import OperationalError





def home(request):
    # Add any necessary logic here
    return render(request, 'firstapp/home.html')
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Debug: Print entered username and password
            print(f"Entered Username: {username}, Entered Password: {password}")

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                message = f"Welcome, {user.username}!"
                return redirect('result')# Redirect to home page after successful login
            else:
                print("Authentication failed: User is None")
                form.add_error(None, "Invalid username or password")
        else:
            print("Form is not valid")
    else:
        form = AuthenticationForm()
    return render(request, 'firstapp/login.html', {'form': form})

def add_expense_view(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            # Save form data to MySQL database
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='Mysqljobde@5',
                database='expense_db'
            )
            cursor = connection.cursor()

            # Example: Insert new expense into MySQL
            query = "INSERT INTO firstapp_expense (title, amount, category, date) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (form.cleaned_data['title'], form.cleaned_data['amount'], form.cleaned_data['category'], form.cleaned_data['date']))
            connection.commit()

            cursor.close()
            connection.close()

            # Redirect to expense_list view after adding expense
            return redirect('expense_list')
    else:
        form = ExpenseForm()

    return render(request, 'firstapp/add_expense.html', {'form': form})
from django.shortcuts import render
import mysql.connector
from mysql.connector import Error

def expense_list(request):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Mysqljobde@5',
            database='expense_db'
        )
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM firstapp_expense")
            expenses = cursor.fetchall()
            cursor.close()
            connection.close()
            return render(request, 'firstapp/expense_list.html', {'expenses': expenses})
        else:
            return render(request, 'error.html', {'message': 'Database connection failed.'})
    except Error as e:
        print(f"Error connecting to database: {e}")
        return render(request, 'error.html', {'message': 'Database error occurred.'})


def result(request):
    # Example data (replace with your own data)
    # result_data = {
    #     'message': 'Your result message goes here!',
    #     'data': ['Expense 1', 'Expense 2', 'Expense 3'],  # Example list of expenses
    # }

    # Render the template 'result.html' with the provided context data
    return render(request, 'firstapp/result.html')
