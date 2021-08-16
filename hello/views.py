from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.


def index(request):
    return render(request, "hello/index.html")


def members(request):
    now = datetime.datetime.now()
    return render(request, "hello/members.html", {"name": now.month == 6 and now.day == 27})


# def greet(request, name):
#     return HttpResponse(f'hellO whatsApp {name}')
