from django.conf.urls import url, include
from . import views

urlpatterns = [
     url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
     url(r'^$', views.index, name='index'),
     url(r'^search/$', views.Search, name='search'),
     url(r'^cookie/$', views.CookiesKangaroo.test_cookie, name='cookie'),
     url(r'^track_user/$', views.CookiesKangaroo.track_user, name='track_user'),
     url(r'^stop_tracking/$', views.CookiesKangaroo.stop_tracking, name='stop_tracking'),
     url(r'^test_delete/$', views.SessionsKangaroo.test_delete, name='test_delete'),
     url(r'^test_session/$', views.SessionsKangaroo.test_sesstion, name='test_session'),
     url(r'^save-session-data/$', views.SessionsKangaroo.save_session_data, name='save-session-data'),
     url(r'^access-session-data/$', views.SessionsKangaroo.access_session_data, name='access_session-data'),
     url(r'^delete-session-data/$', views.SessionsKangaroo.delete_session_data, name='delete-session-data'),
     url(r'^lousy-login/$', views.LousyKangaroo.lousy_login, name='lousy_login'),
    url(r'^lousy-secret/$', views.LousyKangaroo.lousy_secret, name='lousy_secret'),
    url(r'^lousy-logout/$', views.LousyKangaroo.lousy_logout, name='lousy_logout'),
]