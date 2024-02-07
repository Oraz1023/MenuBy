from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "index.html")

def menuby(request, pk):
    # ваша логика представления здесь
    return HttpResponse('Menu by pk: {}'.format(pk))
