from django.shortcuts import render, get_object_or_404, render_to_response
from django.utils import timezone
from .models import Articles
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.shortcuts import redirect
from django.contrib import messages, auth
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic.base import View

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


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/account')
    else:
        form = UserCreationForm()
        args = {'form': form}
        return render(request, 'accounts/reg_form.html', args)


from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render_to_response

def search(request):
     q = request.GET['q']
     if q:
         result = Articles.objects.filter(
             Q(title__icontains=q)|
             Q(body__icontains=q))
     else:
         result = False

     return render_to_response ('homepage/search.html',
                              {"result": result, 'q': q})


#Q(нужноеполе_in=[слово1, слово2])