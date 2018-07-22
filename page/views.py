from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.utils import timezone
from .models import Articles, Genre
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages, auth
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from django.views.generic.base import View
from django import forms
from django.db.models import Q
import re
from taggit.models import Tag


def index(request, tag_slug=None):
    posts = Articles.objects.filter(date__lte=timezone.now()).order_by('-date')
    last_post = None

    if len(posts) > 0:
        last_post = posts[0]
        if len(posts) >= 5:
            paginator = Paginator(posts, 5)
        else:
            paginator = Paginator(posts, len(posts))
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


def search(request):
    q = request.GET['q']
    res = [i for i in q.split()]
    cash = []
    result = []
    add_res = []
    if q:
        result = []
        for j in res:
            if j not in cash:
                cash.append(j)
                result.append(Articles.objects.filter(
                    Q(title__icontains=j) |
                    Q(body__icontains=j)))

    if len(result) > 0:
        add_res = [i for i in result[-1]]
        if len(add_res) > 1:
            add_res = add_res[-1]
        if len(result) >= 30:
            paginator = Paginator(result, 30)
        else:
            paginator = Paginator(result, len(result))
        page = request.GET.get('page')
        try:
            result = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            result = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            result = paginator.page(paginator.num_pages)
    return render_to_response('homepage/search.html',
                              {"result": result, "add_res": add_res, 'q': q})


def handler404(request):
    return HttpResponseNotFound(
        render(request, "errors/404.html")
    )


class Information():
    def developers(request):
        return render(request, 'homepage/developers.html')


class Contacts():
    def contacts(request):
        return render(request, 'homepage/contacts.html')


def search_list(request):
    return render(request, 'homepage/search.html')


def show_genres(request):
    return render(request, "homepage/category.html", {'genres': Genre.objects.all()})


def move_category(request, id):
    target = get_object_or_404(Genre, pk=id)
    return render(request, 'homepage/category.html', {'target': target})
