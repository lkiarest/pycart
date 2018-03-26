from django.conf.urls import url

from . import views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'login$', TemplateView.as_view(template_name='dashboard/login.html')),
    url('users', views.UserList.as_view()),
    url(r'^$', views.IndexView.as_view()),
]
