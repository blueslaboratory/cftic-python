from django.utils.timezone import datetime
from django.shortcuts import render
import pandas as pd

# Create your views here.
from django.http import HttpResponse 


def home(request):
    return HttpResponse("Hello, Django!")

def hello_there(request, name):
    print(request.build_absolute_uri()) #optional
    personas = pd.read_csv('datos.csv')
    return render(
        request,
        'hello/hello_there.html',
        {
            'name': name,
            'date': datetime.now(),
            'personas': personas,
        }
    )