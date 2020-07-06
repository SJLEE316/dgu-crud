from django.shortcuts import render

# Create your views here.

def address(request):
    return render(request, 'home/address.html')

def design(request):
    return render(request, 'home/design.html')

def phone(request):
    return render(request, 'home/phone.html')