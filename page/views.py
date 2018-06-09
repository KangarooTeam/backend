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
from django.http import HttpResponse
from django.shortcuts import render_to_response

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

def test_cookie(request):   
    if not request.COOKIES.get('color'):
        response = HttpResponse("Cookie Set")
        response.set_cookie('color', 'blue', 3600 * 24 * 365 * 2)
        return response
    else:
        return HttpResponse("Your favorite color is {0}".format(request.COOKIES['color']))

def track_user(request):
    if not request.COOKIES.get('visits'):
        response = HttpResponse("This is your first visit to the site. "
                                "From now on I will track your vistis to this site.")
        response.set_cookie('visits', '1', 3600 * 24 * 365 * 2)
    else:
        visits = int(request.COOKIES.get('visits')) + 1
        response = HttpResponse("This is your {0} visit".format(visits))
        response.set_cookie('visits', str(visits),  3600 * 24 * 365 * 2)
    return response

def stop_tracking(request):
    if request.COOKIES.get('visits'):
       response = HttpResponse("Cookies Cleared")
       response.delete_cookie("visits")
    else:
        response = HttpResponse("We are not tracking you.")
    return response

"""
def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        query = q.split()
        result = []
        for q in query:
            result_title = Articles.objects.filter(title__icontains=q)
            result_body = Articles.objects.filter(body__icontains=q)
            result.append(result_body)
            result.append(result_title)
            result.split()
           if result_title:
                return render_to_response ('homepage/search_results.html',
                    {'result_title': result_title, 'query': q})
            if result_body:
            return render_to_response ('homepage/search_results.html',
                    {'result': result})
                    """

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        query = q.split()
        for q in query:
            result_title = Articles.objects.filter(title__icontains=q)
            result_body = Articles.objects.filter(body__icontains=q)
            if result_title:
                return render_to_response ('homepage/search_results.html',
                    {'result_title': result_title, 'query': q})
            if result_body:
                return render_to_response ('homepage/search_results.html',
                    {'result_body': result_body})
    else:
        return HttpResponse('Please submit a search term.')
# BAD!
def bad_search(request):
    # The following line will raise KeyError if 'q' hasn't
    # been submitted!
    message = 'You searched for: %r' % request.GET['q']
    return HttpResponse(message)