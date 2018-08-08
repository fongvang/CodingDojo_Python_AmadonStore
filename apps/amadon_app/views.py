from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def index(request):
    context = { "items" : items.objects.all() }
    if "total" not in request.session:
        request.session['total'] = 0
        request.session['charged'] = 0
        request.session['items'] = 0
    return render(request, 'index.html', context)

def process(request):
    if 'total' in request.session:
        request.session['charged'] = float(request.POST['price']) * int(request.POST['quantity'])
        request.session['items'] = request.POST['quantity'] + str(request.session['items'])
        request.session['total'] += float(request.session['charged'])

    return redirect('/checkout')

def checkout(request):
    return render(request, "checkout.html")

def home(request):
    return redirect('/')
