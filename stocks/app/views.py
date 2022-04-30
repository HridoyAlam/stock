from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import requests
from .forms import NameForm

# Create your views here.
def home(request):
    import requests
    import json
    api_request = requests.get("https://cloud.iexapis.com/stable/stock/aapl/quote?token=pk_0f23852bc2214eecb55dea7c1ffb8cba")
    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "...Error....."

    return render(request, "home.html", {'api':api})

def about(request):
    return render(request, "about.html", {})

def test(request):
    return render(request, "test.html", {})

def page1(request):
    return render(request, "d_page1.html", {})

def page2(request):
    results = request.GET['model']
    print(results)
    return render(request, "d_page2.html", {'model': results})

def get_name(request):
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("name")
    else:
        form = NameForm()
    context = {
        'form_key': form
    }
    return render(request, 'name.html', context)


def profile(request):
    return render(request, "profile.html", {})

# pk_0f23852bc2214eecb55dea7c1ffb8cba 
# aapl
# TSLA