from django.conf.urls import url, include
from . import views


urlpatterns = [
     url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
     url(r'^$', views.index, name='index'),
     url(r'^search/$', views.search, name='search'),
     url(r'^register/$', views.register, name='register'),
     url(r'^login/$', views.log_in, name='log_in'),
     url(r'^developers/$', views.developers, name="developers"),
     url(r'^contacts/$', views.contacts, name='contacts'),
]

