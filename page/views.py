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


class CookiesKangaroo:

    def test_cookie(self, request):   
        if not request.COOKIES.get('color'):
            response = HttpResponse("Cookie Set")
            response.set_cookie('color', 'blue', 3600 * 24 * 365 * 2)
            return response
        else:
            return HttpResponse("Your favorite color is {0}".format(request.COOKIES['color']))

    def track_user(self, request):
        if not request.COOKIES.get('visits'):
            response = HttpResponse("This is your first visit to the site. "
                                    "From now on I will track your vistis to this site.")
            response.set_cookie('visits', '1', 3600 * 24 * 365 * 2)
        else:
            visits = int(request.COOKIES.get('visits')) + 1
            response = HttpResponse("This is your {0} visit".format(visits))
            response.set_cookie('visits', str(visits),  3600 * 24 * 365 * 2)
        return response

    def stop_tracking(self, request):
        if request.COOKIES.get('visits'):
            response = HttpResponse("Cookies Cleared")
            response.delete_cookie("visits")
        else:
            response = HttpResponse("We are not tracking you.")
        return response

class SessionsKangaroo:

    def test_sesstion(self, request):
        request.session.set_test_cookie()
        return HttpResponse("Testing session cookie")

    def test_delete(self, request):
        if request.session.test_cookie_worked():
            request.session.delete_test_cookie()
            response = HttpResponse("Cookie test passed")
        else:
            response = HttpResponse("Cookie test failed")
        return response

    def save_session_data(self, request):
        request.session['id'] = 1
        request.session['name'] = 'root'
        request.session['password'] = 'rootpass'
        return HttpResponse("Session Data Saved")


    def access_session_data(self, request):
        response = ""
        if request.session.get('id'):
            response += "Id : {0} <br>".format(request.session.get('id'))
        if request.session.get('name'):
            response += "Name : {0} <br>".format(request.session.get('name'))
        if request.session.get('password'):
            response += "Password : {0} <br>".format(request.session.get('password'))

        if not response:
            return HttpResponse("No session data")
        else:
            return HttpResponse(response)

    def delete_session_data(self, request):
        try:
            del request.session['id']
            del request.session['name']
            del request.session['password']
        except KeyError:
            pass
        
        return HttpResponse("Session Data cleared")

class LousyKangaroo:
    def lousy_login(self, request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            if username == "root" and password == "pass":
                request.session['logged_in'] = True
                return redirect('lousy_secret')
            else:
                messages.error(request, 'Error wrong username/password')
        return render(request, 'lousy/lousy_login.html')


    def lousy_secret(self, request):
        if not request.session.get('logged_in'):
            return redirect('lousy_login')
        return render(request, 'lousy/lousy_secret_page.html')


    def lousy_logout(self, request):
        try:
            del request.session['logged_in']
        except KeyError:
            return redirect('lousy_login')
        return render(request, 'lousy/lousy_logout.html')


from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render_to_response

def search(request):
     q = request.GET['q']
     result = Articles.objects.filter(
         Q(title__icontains=q)|
         Q(body__icontains=q))
     return render_to_response ('homepage/search.html',
                              {"result": result, 'q': q})


