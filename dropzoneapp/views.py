from django.shortcuts import render
from django.http import HttpResponse

"""def index(request):
    return HttpResponse("deneme")"""

def index(request):
    return render(request, 'dropzoneapp/index.html')
