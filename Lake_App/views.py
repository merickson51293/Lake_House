from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def bakeshophome(request):
    return render(request, "bakeshophome.html")

def giftshophome(request):
    return render(request, "giftshophome.html")

def printshophome(request):
    return render(request, "printshophome.html")