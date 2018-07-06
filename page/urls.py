from django.conf.urls import url, include
from . import views


urlpatterns = [
     url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
     url(r'^$', views.index, name='index'),
     url(r'^search/$', views.search, name='search'),
     url(r'^search_list/$', views.search_list, name="search_list"),
     url(r'^register/$', views.register, name='register'),
     url(r'^login/$', views.log_in, name='log_in'),
     url(r'^developers/$', views.Information.developers, name="developers"),
     url(r'^contacts/$', views.Contacts.contacts, name='contacts'),
     ]

