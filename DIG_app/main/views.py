from django.shortcuts import render
from django.http import HttpResponse
from .models import Establecimiento, Usuario

# Create your views here.
def homepage(request):
    return render(request=request, 
                  template_name='main/index.html',
                  context={ "establecimientos": Establecimiento.objects.all })

def cities(request):
    return HttpResponse("Currently you are in  <strong>CITY</strong>, to change click the button below.")