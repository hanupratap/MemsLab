from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from memslab.models import Employee


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class LoginForm(forms.ModelForm):    
    class Meta:
        model = User
        fields = ('username','password')

class ProfilePic(forms.ModelForm): 
    class Meta:
        model = Employee
        fields = ('emp_pic',)
          