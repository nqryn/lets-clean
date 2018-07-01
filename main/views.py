from django.shortcuts import render, redirect


def home(request):
    return render(request, "main/home_customer.html")

def home_manager(request):
    return render(request, "main/home_manager.html")