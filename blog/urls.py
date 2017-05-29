from django.conf.urls import url
from . import views

app_name = 'blog'

urlpatterns = [
    url(r'^$', views.post_list.as_view(), name='post_list'),

    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail.as_view(), name='post_detail'),

    url(r'^post/new/$', views.post_new.as_view(), name='post_new'),

    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit.as_view(), name='post_edit'),

    url(r'^post/(?P<pk>[0-9]+)/delete/$', views.post_delete.as_view(), name='post_delete'),
]