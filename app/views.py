from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from app.decorators import allowed_users, unauthenticated_user
import yfinance as yf

from app.forms import CreateUserForm, InvestForm, CreateForm

# User Interfacing
@unauthenticated_user
def registerpage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {'form':form}
    return render(request, 'register.html', context)

@unauthenticated_user
def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home-page')
        else:
            messages.info(request, 'Username OR Password is incorrect')

    context = {}
    return render(request, 'login.html', context)

def logoutpage(request):
    logout(request)
    return redirect('login')

# Home Page
@login_required(login_url='login')
#@allowed_users(allowed_roles='admin')
def home(request):

    context = {'ticks': ['AMZN', 'AAPL', 'MSFT', 'BOMN', 'ABNB']}
    return render(request, 'home.html', context)

def portfoliopage(request):
    
    context = {}
    return render(request, 'portfolio.html', context)

def stockpage(request):
    form = CreateForm()
    if request.method == 'POST':
        form = CreateForm(data=request.POST)
        if form.is_valid():
            ticker_name = form.cleaned_data['ticker']
            ticker = yf.Ticker(ticker_name)
    return render(request, 'stocks.html', {'ticker': ticker})

def investment(request):
    form = InvestForm()
    if request.method == 'POST':
        form = InvestForm(request.POST)
        if form.is_valid():
            instance = form.save()
            instance.user = request.user
            instance.stock = request.stock
            instance.save()
            return redirect('home-page')

    context = {'form': form}
    return render(request, 'invest_page.html', context)

def sell(request):
    ...