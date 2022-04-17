from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, "home.html", {})

def about(request):
    return render(request, "about.html", {})


# pk_0f23852bc2214eecb55dea7c1ffb8cba