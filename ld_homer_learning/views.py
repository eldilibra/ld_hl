from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'ld_homer_learning/index.html')
