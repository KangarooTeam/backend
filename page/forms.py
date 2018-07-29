from django import forms
from page.models import Articles
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    image = forms.ImageField(label='Аватар', required=False)
    email = forms.CharField(max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput(), label='Пароль')
    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email', 'image')

class UserFormForEdit(forms.ModelForm):
    image = forms.ImageField(label='Аватар', required=False)
    email = forms.CharField(max_length=100, required=True)
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Articles
        exclude = ('tags', 'category', 'image')
