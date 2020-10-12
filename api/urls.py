from django.urls import path, include

from . import views
from django.conf.urls import url

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path('restricted/', views.restricted, name='restricted'),

]