from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import (UserCreationForm, UserChangeForm)
from memslab.models import Employee, Project, News
from django.utils.safestring import mark_safe

 
class DateInput(forms.DateInput):
    input_type = 'date'

 
class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(
        max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(
        max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2', )

    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()

        return user


class LoginForm(forms.ModelForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    username=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'password')
 

class ProfilePic(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('emp_pic',)


class EditUserForm(UserChangeForm):

    class Meta:
        model = User
        fields = (
            'email', 'first_name', 'last_name', 'username',
        )


class Project_add(forms.ModelForm):
    class Meta:
        model = Project
        exclude = []
        widgets = {
        'created_at': DateInput,
        'completed_at': DateInput,
        }

        

class News_add(forms.ModelForm):
    class Meta:
        model = News
        exclude = ['user']

