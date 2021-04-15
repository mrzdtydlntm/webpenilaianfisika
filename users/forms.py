from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, PasswordChangeForm
    
class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput)
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'email',
            'password1',
            'password2'
        ]
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
    
class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput)
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'email',
            'password',
        ]

class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'type':'password'}))
    new_password1 = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'type':'password'}))
    new_password2 = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'type':'password'}))
    class Meta:
        model = User
        fields = [
            'old_password',
            'new_password1',
            'new_password2'
        ]
    def __init__(self, *args, **kwargs):
        super(PasswordChangingForm, self).__init__(*args, **kwargs)
        self.fields['old_password'].label = "Password Lama"
        self.fields['new_password1'].label = "Password Baru"
        self.fields['new_password2'].label = "Konfirmasi Password Baru"
