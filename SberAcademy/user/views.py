from django.shortcuts import render
from django.views.decorators.cache import cache_control
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User


@login_required(login_url='/user/login/')
@cache_control(no_cache=True, must_revalidate=True)
def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/user/login')

@login_required(login_url='/user/login/')
def profile(request, user_id):
    user = User.objects.get(id=user_id)
    return render(request, 'user/profile.html', {'user': user})