from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,"index.html")

def basic(request):
    return render(request,'basic.html')


def blog(request):
    return render(request, 'blog.html')

def cart(request):
    return render(request,"cart.html")


def category(request):
    return render(request, "category.html")

def checkout(request):
    return render(request, "checkout.html")

def confirmation(request):
    return render(request, "confirmation.html")


def contact(request):
    return render(request, "contact.html")


def elements(request):
    return render(request, "elements.html")


def login(request):
    return render(request, "login.html")

def single_blog(request):
    return render(request, "single-blog.html")

def single_product(request):
    return render(request, "single-product.html")

def tracking(request):
    return render(request, "tracking.html")