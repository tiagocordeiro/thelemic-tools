from django.shortcuts import render

from .facade import resh_hours
from .models import CustomLocation


# Create your views here.
def resh_hours_list(request):
    horario_pratica = resh_hours("Santo André, SP", "Brasil", -23.63434, -46.53395, "America/Sao_Paulo", 756)
    context = {'ra': horario_pratica['Nascer do sol'].strftime("%H:%M:%S"),
               'ahathoor': horario_pratica['Meio-dia solar'].strftime("%H:%M:%S"),
               'tum': horario_pratica['Pôr do sol'].strftime("%H:%M:%S"),
               'kephera': horario_pratica['Meia-noite solar'].strftime("%H:%M:%S")}
    return render(request, 'resh/hours.html', {'context': context})


def resh_hours_list_saved_location(request, location_id):
    custom_local = CustomLocation.objects.get(pk=location_id)
    horario_pratica = resh_hours(local_name=custom_local.name, region=custom_local.region,
                                 latitude=float(custom_local.latitude), longitude=float(custom_local.longitude),
                                 time_zone=custom_local.time_zone, elevation=int(custom_local.elevation))
    context = {'ra': horario_pratica['Nascer do sol'].strftime("%H:%M:%S"),
               'ahathoor': horario_pratica['Meio-dia solar'].strftime("%H:%M:%S"),
               'tum': horario_pratica['Pôr do sol'].strftime("%H:%M:%S"),
               'kephera': horario_pratica['Meia-noite solar'].strftime("%H:%M:%S")}
    return render(request, 'resh/hours.html', {'context': context})


def resh_hours_list_custom_location(request, name, region, latitude, longitude, time_zone, elevation):
    tzfix = time_zone.replace('-', '/')
    horario_pratica = resh_hours(local_name=name, region=region,
                                 latitude=float(latitude), longitude=float(longitude),
                                 time_zone=tzfix, elevation=int(elevation))
    context = {'ra': horario_pratica['Nascer do sol'].strftime("%H:%M:%S"),
               'ahathoor': horario_pratica['Meio-dia solar'].strftime("%H:%M:%S"),
               'tum': horario_pratica['Pôr do sol'].strftime("%H:%M:%S"),
               'kephera': horario_pratica['Meia-noite solar'].strftime("%H:%M:%S")}
    return render(request, 'resh/hours.html', {'context': context})
