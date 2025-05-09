from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import LoginForm, RegisterForm
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    category_counts = {
        'vegetables_count': Product.objects.filter(category='Vegetables').count(),
        'fruits_count': Product.objects.filter(category='Fruits').count(),
        'meat_count': Product.objects.filter(category='Meat').count(),
        'fish_count': Product.objects.filter(category='Fish').count(),
        'spices_count': Product.objects.filter(category='Spices').count(),
    }
    return render(request, 'index.html', category_counts)

def product(request):
    categories = ['Vegetables', 'Fruits', 'Meat', 'Fish', 'Spices']
    categorized_products = {
        category: Product.objects.filter(category=category)[:5]
        for category in categories
    }
    return render (request, 'Products.html', {'categorized_products': categorized_products})


def category_detail(request, category):
    products = Product.objects.filter(category=category)
    return render(request, f'{category}.html', {'products': products, 'category': category})


def vegetable(request):
    products = Product.objects.filter(category='vegetables')
    return render(request, "Vegetables.html", {'products': products})


def fruit(request):
    return render(request, "Fruits.html")


def meat(request):
    return render(request, "Meat.html")



def river_fish(request):
    return render(request, "Fish.html")


def spice(request):
    return render(request, "Spices.html")

def create_plan(request):
    days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    return render(request, 'CreatePlan.html', {'days': days})

def select_product(request):
    return render(request, 'SelectProduct.html')

def checkout(request):
    return render(request, 'checkout.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                username = User.objects.get(email=email).username  # get username via email
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, "Login successful!")
                    return redirect('index')  # 🔁 change to your homepage name
                else:
                    messages.error(request, "Invalid credentials")
            except User.DoesNotExist:
                messages.error(request, "No user with that email")
    else:
        form = LoginForm()
    return render(request, 'registration/Login.html', {'form': form})



def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')  # change if needed
    else:
        form = RegisterForm()
    return render(request, 'registration/CreateAccount.html', {'form': form})



def checkout(request):
    return render(request, "checkout.html")