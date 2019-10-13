from django.urls import path

from . import views

urlpatterns = [
    path('hours/',
         views.resh_hours_list,
         name='resh_hours_list'),
    path('hours/<int:location_id>/',
         views.resh_hours_list_saved_location,
         name='resh_hours_list_saved_location'),
    path('hours/<name>/<region>/<latitude>/<longitude>/<time_zone>/<elevation>',
         views.resh_hours_list_custom_location,
         name='resh_hours_list_custom_location')
]
