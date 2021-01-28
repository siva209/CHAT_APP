from django.urls import path

from chatapp.views import hello

urlpatterns = [
    path('hello/', hello, name='hello')
    ]