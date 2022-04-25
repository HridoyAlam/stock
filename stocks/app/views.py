from django.shortcuts import render


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


# pk_0f23852bc2214eecb55dea7c1ffb8cba 
# aapl
# TSLA