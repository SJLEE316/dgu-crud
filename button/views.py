from django.shortcuts import render

# Create your views here.

def dongari(request):
    return render(request, 'button/dongari.html')

def volun(request):
    return render(request, 'button/volun.html')
