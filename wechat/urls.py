from django.conf.urls import url
from django.urls import path, re_path

from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('/login', views.LoginView.as_view()),
    re_path('^$', views.IndexView.as_view()),
]
