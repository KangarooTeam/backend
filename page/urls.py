from django.conf.urls import url, include
from . import views

urlpatterns = [
     url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
     url(r'^$', views.index, name='index'),
     url(r'^register/', views.RegisterFormView.as_view())
]