from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
def calculate(request):
    return render(request, 'calculate.html')
