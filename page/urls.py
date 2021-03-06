from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
     url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
     url(r'^$', views.index, name='index'),
     url(r'^search/$', views.search, name='search'),
     url(r'^search_list/$', views.search_list, name="search_list"),
     url(r'^category/$', views.show_genres, name="category"),
     url(r'^target_category/(?P<pk>[0-9]+)/$', views.move_category, name="target_category"),
     url(r'^developers/$', views.Information.developers, name="developers"),
     url(r'^contacts/$', views.Contacts.contacts, name='contacts'),
     ]

