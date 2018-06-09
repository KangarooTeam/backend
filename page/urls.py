from django.conf.urls import url, include
from . import views

urlpatterns = [
     url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
     url(r'^$', views.index, name='index'),
     url(r'^search/$', views.search, name='search'),
     url(r'^cookie/$', views.test_cookie, name='cookie'),
     url(r'^track_user/$', views.track_user, name='track_user'),
     url(r'^stop_tracking', views.stop_tracking, name='stop_tracking'),
]