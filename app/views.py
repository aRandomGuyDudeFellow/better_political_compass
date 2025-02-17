from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
    questions = Question.objects.order_by("index")
    output = ", ".join([q.text for q in questions])
    return HttpResponse(output)