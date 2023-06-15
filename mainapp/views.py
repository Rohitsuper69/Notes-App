from django.shortcuts import render

def home_page(request):
    return render(request,"home-view.html",{})

def create_view(request):
    return render(request,"create.html",{})

def check_view(request):
    return render(request,"check.html",{})