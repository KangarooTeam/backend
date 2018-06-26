from django.shortcuts import render, get_object_or_404, render_to_response
from django.utils import timezone
from .models import Articles
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect
from django.contrib import messages, auth
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic.base import View
from django import forms
from django.http import HttpResponseNotFound

def index(request):
    posts = Articles.objects.all()
    posts_r = [r for r in reversed(posts)]
    last_post = None
    if len(posts_r) > 0:
        last_post = posts_r[0]
        paginator = Paginator(posts_r, 3)
        page = request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            posts = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            posts = paginator.page(paginator.num_pages)
    return render(request, 'homepage/wrapper.html', {'posts': posts, "last_post": last_post})


def post_detail(request, pk):
    post = get_object_or_404(Articles, pk=pk)
    return render(request, 'homepage/post_detail.html', {'post': post})

class LoginForm(forms.Form):
    username = forms.CharField(label=u'Имя пользователя')
    password = forms.CharField(label=u'Пароль', widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        if not self.errors:
            user = authenticate(username=cleaned_data['username'], password=cleaned_data['password'])
            if user is None:
                raise forms.ValidationError(u'Имя пользователя и пароль не подходят')
            self.user = user
        return cleaned_data

    def get_user(self):
        return self.user or None

def log_in(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            if form.get_user():
                login(request, form.get_user())
                return HttpResponseRedirect('/')
    else:
        form = LoginForm()
    return render(request, 'accounts/log_form.html', {'form': form})

class RegistrationForm(forms.Form):
    username = forms.CharField(label='Имя пользователя')
    password1 = forms.CharField(label=u'Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label=u'Повторите пароль', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        # TODO: проверить, что username не занят
        return self.cleaned_data

    def clean(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        # TODO: проверить, что пароли совпадают
        return self.cleaned_data

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # TODO:
            # 1. создать пользователя,
            # 2. установить ему пароль
            # 3. Зайти под его именем на сайт
            return HttpResponseRedirect('/')

    else:
        form = RegistrationForm()
    return render(request, 'accounts/reg_form.html', {'form': form})

# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/account')
#     else:
#         form = UserCreationForm()
#         args = {'form': form}
#         return render(request, 'accounts/reg_form.html', args)


from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render_to_response
import re

def search(request):
     q = request.GET['q']
     res = [i for i in q.split()]
     if q:
         result = []
         cash = []
         for j in res:
             result.append(Articles.objects.filter(
                 Q(title__icontains=j)|
                 Q(body__icontains=j)))
     else:
         result = False

     return render_to_response ('homepage/search.html',
                              {"result": result, 'q': q})


#Q(нужноеполе_in=[слово1, слово2])

def handler404(request):
    return HttpResponseNotFound(
        render(request, "errors/404.html")
    )

def developers(request):
    return render(request, 'homepage/developers.html')

def contacts(request):
    return render(request, 'homepage/contacts.html')

