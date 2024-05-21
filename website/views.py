from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import *
from . import models

# Create your views here.
def home(request):
    # Check if user is logging in
    customers = models.Customer.objects.all()

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in!')
            return redirect('website:home')
        else:
            messages.success(request, 'There was an error logging in... Please Try again!')
            return redirect('website:home')
    else:
        return render(request, 'website/home.html', {
            "customers": customers
        })

def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('website:home')

def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate user
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, 'You have successfully registered! Welcome to CRM')
            return redirect('website:home')
    else:
        form = SignUpForm()

    return render(request, 'website/register.html',  {
        "form": form
    })

def customer_page(request, pk):
    # Show User record if logged in
    if request.user.is_authenticated:
        customer = models.Customer.objects.get(id=pk)
        return render(request, 'website/customer.html', {
            "customer": customer
        })
    else:
        messages.success(request, "You must be logged in to view this page... Sorry!")
        return redirect('website:home')
    
def delete_customer(request, pk):
    if request.user.is_authenticated:
        customer = models.Customer.objects.get(id=pk)
        customer.delete()
        messages.success(request, "Customer Deleted Successfully...")
        return redirect('website:home')
    else:
        messages.success(request, "You must be logged in to do this action!")
        return redirect('website:home')

        
