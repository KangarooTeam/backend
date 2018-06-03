from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Articles
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.contrib.auth import logout

def index(request):
    posts = Articles.objects.all()
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)
    return render(request, 'homepage/wrapper.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Articles, pk=pk)
    return render(request, 'homepage/post_detail.html', {'post': post})

class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = "/login/"
    template_name = "homepage/register.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)

class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "homepage/login.html"
    success_url = "/"

    def form_valid(self, form):
        self.user = form.get_user()

        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)

class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")