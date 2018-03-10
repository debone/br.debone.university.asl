from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('timeslot/new', views.timeslot_create, name='get_name'),
    path('timeslot/', views.index, name='thanks')
]