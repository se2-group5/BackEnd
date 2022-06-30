from dataclasses import field
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import OccupationStatus, User, Report, Business

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True): # commit the data on the SQL DB
        user = super(NewUserForm, self).save(commit=False) # Don't want to commit just yet, we need to create an user object save it in python.
        user.email = self.cleaned_data['email'] 

        if commit:
            user.save() # then we commit in DB
        return user


class ReportForm(forms.ModelForm):
    occupation_status = forms.ModelChoiceField(queryset=OccupationStatus.objects.all(),
                                    to_field_name="status",
                                    empty_label="Select occupation")
    
    class Meta:
        model = Report
        fields = "__all__"
        # fields = ('occupation_status', 'internet_status', 'rating_business', 'comments')
