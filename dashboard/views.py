from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
# from django.contrib.auth.decorators import login_required
# from django.utils.decorators import method_decorator
from user.models import User

# decorators = [login_required]

# Create your views here.
# @method_decorator(decorators, name='dispatch')
class IndexView(TemplateView):
    name = 'Hello World'
    template_name = 'dashboard/index.html'

    def get(self, request):
        return HttpResponse(self.name)

class UserList(ListView):
    # model = User
    context_object_name = 'user_list'
    template_name = 'dashboard/users.html'
    queryset = User.objects.order_by('-id')
    paginate_by = 10
