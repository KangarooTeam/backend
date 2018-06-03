from django.conf.urls import url, include
from . import views

urlpatterns = [
     url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
     url(r'^$', views.index, name='index'),
     url(r'^search-form/$', views.search_form),
     url(r'^search/$', views.search),
     url(r'^register/', views.RegisterFormView.as_view())
]