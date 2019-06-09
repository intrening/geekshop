from django.shortcuts import render
import json

# Create your views here.

def product_list(request):
    with open('server/products/fixtures/data.json') as file:
        context = json.load(file)
    return render(request, 'products/index.html', {'products':context})

def product_detail (request,pk):
    with open('server/products/fixtures/data.json') as file:
        context = json.load(file)
        
    return render(request, 'products/detail.html', {'product':context[pk]})


