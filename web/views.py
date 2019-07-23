from django.shortcuts import render

# Create your views here.
from web.models import network, user
from .forms import ConfigForm
from web.configuration import saveConfig

def index(request):
    return render(request, 'web/index.html')

def table(request):
    return render(request, 'web/devices.html', {'users': [user("24-8D-76-FD-72-18"), user('2F-EB-B9-5D-B6-DF')]})

def config(request):
    if request.method == 'POST':
        form = ConfigForm(request.POST)
        if form.is_valid():

            print(form.cleaned_data['network'])
            saveConfig(form.cleaned_data['network'])

            return render(request, 'web/devices.html', {'users': []})
    else:
        form = ConfigForm()
        return render(request, 'web/config.html', {'form': form})


