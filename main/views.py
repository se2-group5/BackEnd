from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.urls import reverse
from .models import *
from .forms import NewUserForm
from rest_framework import viewsets
from rest_framework.decorators import action    
from .serializers import *
from .forms import NewUserForm, ReportForm
from django.contrib.auth import get_user_model
from django.db.models import Avg


User = get_user_model()

# API

class BusinessView(viewsets.ModelViewSet):
    serializer_class = BusinessSerializer
    queryset = Business.objects.all()

class CityView(viewsets.ModelViewSet):
    serializer_class = CitySerializer
    queryset = City.objects.all()

class ConsultView(viewsets.ModelViewSet):
    serializer_class = ConsultSerializer
    queryset = Consult.objects.all()

class ReportView(viewsets.ModelViewSet):
    serializer_class = ReportSerializer
    queryset = Report.objects.all()

class FavoriteView(viewsets.ModelViewSet):
    serializer_class = FavoriteSerializer
    queryset = Favorite.objects.all()

#  Not using currently
class UserViews(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    @action(methods=['get'], detail=True,url_path='login', url_name='login')
    def login(self, request):
        return []

#######

def login_user(request):
    email = request.GET['email']
    password = request.GET['username']

    user = User.objects.get(email=email)

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
        selected_report = business.report_set.get(pk=request.POST["button_support"]) # Rescata la opción que está en "value" del HTML llamado "button_support" que es el id del objeto de tipo 'Report'.
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

def make_report(request, business_id):
    if request.method == "POST":
        form = ReportForm(data=request.POST)
        if form.is_valid():
            form.save()
            business = get_object_or_404(Business, pk=business_id)
            business.rating= round(Report.objects.filter(business_id__exact=business_id).aggregate(Avg('rating_business'))['rating_business__avg'],1)
            business.internet_quality= round(Report.objects.filter(business_id__exact=business_id).aggregate(Avg('internet_status'))['internet_status__avg'],1)
            business.save()
            return HttpResponseRedirect( reverse("main:biz_profile", args=(business_id, ) ) )
        else:
            messages.error(request, "Invalid form!")


    form = ReportForm()
    return render(request, "main/make_report.html", {
        "form": form,
        })
    
       
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