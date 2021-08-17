from django.shortcuts import render, HttpResponse

# Create your views here.
def login(request):
    return render(request, 'login.html')

def index(request):
    return render(request, 'index.html')

def search(request):
    return render(request, 'search.html')

def upload(request):
    return render(request, 'upload.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def report(request):
    return render(request, 'report.html')
