from django.urls import re_path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    re_path(r'^$', views.start, name='start'),
    re_path(r'^order/$', views.order, name='order'),
    re_path(r'^register/$', views.RegisterFormView.as_view(), name='register'),
    re_path(r'^search/register/$', views.RegisterFormView.as_view(), name='register'),
    re_path(r'^login/$', views.LoginFormView.as_view(), name="login"),
    re_path(r'^logout/$', views.LogoutView.as_view(), name="logout"),
    re_path(r'^jackets/$', views.jackets, name='jackets'),
    re_path(r'^siuts/$', views.siuts, name='siuts'),
    re_path(r'^search/$', views.SearchResultsView.as_view(), name="search"),
    re_path(r'^product/(?P<product_id>\w+)/$', views.product, name='product'),
    re_path(r'^product/(?P<product_id>\w+)/feedback/$', views.MyFeedback.as_view(), name="feedback"),
    re_path(r'^search/feedback/$', views.MyFeedback.as_view(), name="feedback"),
    re_path(r'^product/(?P<product_id>\w+)/register/$', views.RegisterFormView.as_view(), name='register'),

]