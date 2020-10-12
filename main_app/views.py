from django.shortcuts import render
from .models import User, Song, ProfileSong, Genre
from .forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.serializers.json import DjangoJSONEncoder
import json
from django.core import serializers
from celery.schedules import crontab
from celery.task import periodic_task

def index(request):
    return render(request, 'index.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
    return render(request,'registration.html',
                          {'user_form':user_form,
                           'registered':registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'login.html', {})


@login_required
def choose_genres(request):
    # print(genre_list)
    # if request.GET.get('gnum'):
    #     genre_index = request.GET.get('gnum', 0)
    #     curr_genre = Genre.objects.get(pk=genre_index)
    #     return render(request, 'genres.html', {'genre': curr_genre})
    json_data = serializers.serialize("json", Genre.objects.all())
    return render(request, "temp.html", json_data)


@periodic_task(run_every=crontab(hour=11, minute=38))
def dislike_genre(request, genre_id):
    print('worked')
    return render(request, 'genres.html')








