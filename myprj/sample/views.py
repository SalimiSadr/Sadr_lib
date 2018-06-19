from django.shortcuts import render,HttpResponse
from .models import developer

def index(request):
    developers = developer.objects.all()
    return render(request, "sample/index.html",
                  context={
                            "title" : "My lib",
                            "developers": developers
                           })