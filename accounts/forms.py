from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import UserProfile

class UserLoginForm(forms.Form):
    email = forms.EmailField(max_length=150)
    password = forms.CharField(label='Entrez votre mot de passe',                                                      widget=forms.PasswordInput)
class UserCreationForm(forms.ModelForm ):
    password1 = forms.CharField(label='mot de passe',                                                      widget=forms.PasswordInput)
    password2 = forms.CharField(label='confirmer votre mot de passe',                                       widget=forms.PasswordInput)

    class Meta:
        model = UserProfile
        fields = ['email', 'first_name', 'last_name']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('les mots de passe ne concordent pas')
        return password2
    
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data.get('password1'))
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = UserProfile
        fields = ['email', 'first_name', 'last_name', 'password', 'is_active', 'is_staff']
    
    def clean_password(self):
        return self.initial['password']
    