from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('skdue', views.skdue, name='skdue'),
]
