from django.urls import path

from . import views

urlpatterns = [
    path('hours/', views.resh_hours_list, name='resh_hours_list'),
]
