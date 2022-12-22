from django.shortcuts import render

# Create your views here.
def home(request):
    return render (request, 'myapp/home.html')

def chain(request):
    return render (request, 'myapp/chain.html')
def anklet(request):
    return render (request, 'myapp/anklet.html')
def earrings(request):
    return render (request, 'myapp/earrings.html')