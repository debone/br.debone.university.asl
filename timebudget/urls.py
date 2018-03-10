from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name=''),
    path('create/', views.create, name='create_timeslot'),
    path('<int:slot_id>/', views.view, name='view_timeslot')
]