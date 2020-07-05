from django.shortcuts import render

# Create your views here.

def profile(request):
    return render(request, 'others/profile.html')

def photo(request):
    return render(request, 'others/photo.html')

def visit(request):
    return render(request, 'others/visit.html')