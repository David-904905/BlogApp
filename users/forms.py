from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . models import UserProfile
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm

class SignUpForm(UserCreationForm):
    username = forms.CharField(
        max_length=128,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'style':'width:100%; box-sizing:border-box;padding:0.5em',
                'autocomplete':'off'
            }
        )
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'style':'width:100%; padding:0.5em; box-sizing:border-box;',
                'autocomplete':'off'
            }
        )
    )
    password1 = forms.CharField(
        max_length=128,
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'style':'width:100%; padding:0.5em; box-sizing:border-box;',
                'autocomplete':'off'
            }
        )
    )


    password2 = forms.CharField(
        max_length=128,
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'style':'width:100%; padding:0.5em; box-sizing:border-box;',
                'autocomplete':'off'
            }
        )
    )

    # Study this section again
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        for fieldname, field in self.fields.items():
            field.help_text = ''

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=128,
        widget= forms.TextInput(
            attrs={
                'class':'form-control',
                'autocomplete':'off',
                'style':'width:100%; padding:0.5em; box-sizing: border-box;'
            }
        )
    )

    password = forms.CharField(
        max_length=50,
        widget= forms.PasswordInput(
            attrs={
                'class':'form-control',
                'autocomplete':'off',
                'style':'width:100%; padding:0.5em; box-sizing: border-box;'
            }
        )
    )

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image']
    

class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        max_length=254,
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter your email here',
                'style':'padding:0.5em; width:100%; box-sizing:border-box'
            }
        )
    )