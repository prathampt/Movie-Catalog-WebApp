from django.shortcuts import render

def index(request):
    return render(request, 'movieCatalogApp/index.html')

def profile(request):
    return render(request, 'movieCatalogApp/profile.html')
