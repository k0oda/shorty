from django.shortcuts import render, redirect

from .forms import ShortenForm
from .models import Link, Connection

import random
import string

def index(request):
    form = ShortenForm()
    return render(request, 'index.html', {'form': form})

def shorten(request):
    if request.method == 'POST':
        form = ShortenForm(data=request.POST)

        if form.is_valid():
            link = form.save(commit=False)
            link.code = ''.join(random.choice(string.ascii_letters) for i in range(6))
            link.save()

            return redirect('configure', link.code)
    return redirect('index')

def locate(request, code):
    link = Link.objects.get(code=code)
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    connection = Connection(address=ip, link=link)
    connection.save()
    return redirect(link.original_url)

def configure(request, code):
    link = Link.objects.get(code=code)
    connections = Connection.objects.filter(link=link)
    return render(request, 'link.html', {'connections': connections})
