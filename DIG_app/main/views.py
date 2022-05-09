from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Business
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.
def homepage(request):
    return render(request=request, 
                  template_name='main/index.html',
                  context={ "businesses": Business.objects.all })

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("main:homepage")
        else:
            for msg in form.error_messages: # Error handling from the form.
                print(form.error_messages[msg])

    form = UserCreationForm
    return render(request, 
                  "main/register.html",
                  context={"form": form})


def cities(request):
    return HttpResponse("Currently you are in  <strong>CITY</strong>, to change click the button below.")