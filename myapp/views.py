from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse

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
            return HttpResponseRedirect(reverse("logged_in"))
        else:
            messages.error(request, "Invalid Credentials")
            return HttpResponseRedirect("/")

def perform_logout(request):
    logout(request)
    return HttpResponseRedirect("/")

def logged_in(request):
    return render(request, "loggedin.html")