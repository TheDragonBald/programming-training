from django.shortcuts import render
from .models import Request

# Create your views here.

def request_list(request):
    requests = Request.objects.all()
    return render(request, 'main/request_list.html', {'requests' : requests})