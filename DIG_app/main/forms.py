from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

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


