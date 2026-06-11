from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Request
from .forms import RequestForm


# Create your views here.

def request_list(request):
    requests = Request.objects.all()
    return render(request, 'main/request_list.html', {'requests' : requests})

def request_create(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Заявка успешно создана!')
            return redirect('request_list')
    else:
        form = RequestForm()
    return render(request, 'main/request_create.html', {'form': form})