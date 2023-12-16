from django.shortcuts import render
from django.shortcuts import HttpResponse


from django.shortcuts import render

def home(request):
    return render(request, 'index_dark.html')

def resume(request):
    return render(request, 'resume.html')


def portfolio(request):
    return render(request, 'portfolio_dark.html')

def contacts(request):
    return render(request, 'contacts_dark.html')
    