from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name=''),
    path('create/timeslot', views.create, name='create_timeslot'),
    path('<int:slot_id>/', views.view, name='view_timeslot'),
    path('create/task', views.newTask, name='create_task')
]