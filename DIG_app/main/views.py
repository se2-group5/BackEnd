from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.urls import reverse
from .models import Business, Report
from .forms import NewUserForm

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.
def homepage(request):
    return render(request=request, 
                  template_name='main/index.html',
                  context={ "businesses": Business.objects.all })

# USER VIEWS
def register(request):
    if request.method == "POST":
        form = NewUserForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New account created: {username}")
            login(request, user)
            return redirect("main:homepage")

        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

            return render(request = request,
                            template_name = "main/register.html",
                            context={"form":form})

    form = NewUserForm
    return render(request = request,
                  template_name = "main/register.html",
                  context={"form":form})


def logout_request(request):
    logout(request)
    messages.info(request, "Logged Out")
    return redirect("main:homepage")

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.info(request, f'Your logged in as {username}')
                return redirect("main:homepage")
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")

    form = AuthenticationForm()
    return render(request, 
                 "main/login.html", 
                 {"form": form})


def user_profile(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    reports = list( user.report_set.all() )
    number_reports = len(reports)
    #return HttpResponse("Currently you are in  <strong>A USER PROFILE ! ! !</strong>")
    return render(request, "main/user_profile.html", {
        "user" : user,
        "number_reports": number_reports
    })

# BUSINESS VIEWS
def business_profile(request, business_id):
    business = get_object_or_404(Business, pk=business_id)
    #return HttpResponse("Currently you are in  <strong>A BUSINESS</strong>")
    return render(request, "main/biz_detail.html", {
        "business" : business
    })

def support_report(request, business_id):
    business = get_object_or_404(Business, pk=business_id) # Question.objects.get(pk=1) # Handle error for selected question
    
    try: # handle error for selected choice
        selected_report = business.report_set.get(pk=request.POST["button_support"]) # Rescata la opción que está en "value" del HTML llamado "choice" que es el id del objeto de tipo 'Choice'.
        # En el form la clave es: name='button_support' value={{report.id}}
    except(KeyError, Report.DoesNotExist):
        return render(request, "main/biz_profile.html", {
            "business": business,
            "error_message": "No elegiste un reporte"
        })
    else:
        selected_report.report_support += 1
        selected_report.save()
        return HttpResponseRedirect( reverse("main:biz_profile", args=(business.id, ) ) )

# def add_favorite(request, business_id):
#     business = get_object_or_404(Business, pk=business_id) # Question.objects.get(pk=1) # Handle error for selected question
    
#     try: # handle error for selected choice
#         selected_report = business.report_set.get(pk=request.POST["button_support"]) # Rescata la opción que está en "value" del HTML llamado "choice" que es el id del objeto de tipo 'Choice'.
#         # En el form la clave es: name='button_support' value={{report.id}}
#     except(KeyError, Report.DoesNotExist):
#         return render(request, "main/biz_profile.html", {
#             "business": business,
#             "error_message": "No elegiste un reporte"
#         })
#     else:
#         selected_report.report_support += 1
#         selected_report.save()
#         return HttpResponseRedirect( reverse("main:biz_profile", args=(business.id, ) ) )


def cities(request):
    return HttpResponse("Currently you are in  <strong>CITY</strong>, to change click the button below.")