from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse
from myapp import models

# Create your views here.
def render_login(request):
    return render(request, "login.html")

def perform_login(request):
    if request.method != "POST":
        return HttpResponse("Access denied")
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")
        user_obj = authenticate(request, username=username, password = password)
        if user_obj is not None:
            login(request, user_obj)
            return HttpResponseRedirect(reverse("index"))
        else:
            messages.error(request, "Invalid Credentials")
            return HttpResponseRedirect("/")

def perform_logout(request):
    logout(request)
    return HttpResponseRedirect("/")

def index(request):
    customers = models.Customer.objects.all()
    # print(customers)
    context = {
        "customers": customers
    }
    return render(request, "index.html", context)

def add_customers(request):
    if request.method != "POST":
        return HttpResponse("Method not Allowed")
    else:
        """
        json thing:
        {
            "first_name": Kaustubh,
            "last_name": Wankhede,
        
        }
    	"""
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        age = request.POST.get("age")
        email = request.POST.get("email")
        address = request.POST.get("address")
        try:
            customer_obj = models.Customer(first_name=first_name, last_name=last_name, age=age, email=email, address=address)
            print(customer_obj)
            customer_obj.save()
            messages.success(request, "Customer Added Successfully")
            return HttpResponseRedirect(reverse("index"))
        except:
            messages.error(request, "Failed to Add Customer!")
            return HttpResponseRedirect(reverse("index"))