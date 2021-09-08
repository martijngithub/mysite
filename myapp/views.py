from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

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
            return render(request, "loggedin.html")
        else:
            messages.error(request, "Invalid Credentials")
            return HttpResponseRedirect("/")

def perform_logout(request):
    logout(request)
    return HttpResponseRedirect("/")
