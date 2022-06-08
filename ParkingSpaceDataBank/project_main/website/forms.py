from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from .models import Car


# create class here

# For Adding Car Form
class AddCarForm(ModelForm):
    car_model = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Car Name',
                                                            'style': 'margin-bottom: 10px;'}))
    car_manufacturer = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Car Manufacturer',
                                                              'style': 'margin-bottom: 10px;'}))
    car_color = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Car Color',
                                                              'style': 'margin-bottom: 10px;'}))
    plate_num = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Car Plate Number',
                                                              'style': 'margin-bottom: 10px;'}))

    class Meta:
        model = Car
        fields = ('car_model', 'car_manufacturer', 'car_color', 'plate_num')



# For Registration Form
class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email',
                                                            'style': 'margin-bottom: 10px;'}))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                              'placeholder': 'Enter your first name',
                                                                              'style': 'margin-bottom: 10px;'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                             'placeholder': 'Enter your last name',
                                                                             'style': 'margin-bottom: 10px;'}))

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder': 'This is an email'}))
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                                    'placeholder': 'Enter your password',
                                                                                    'style': 'margin-bottom: 10px;'}))
    password2 = forms.CharField(label="Password Confirmation",
                                widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'placeholder': 'Repeat your password',
                                                                  'style': 'margin-bottom: 10px;'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
