from django.shortcuts import render

from .facade import resh_hours


# Create your views here.
def resh_hours_list(request):
    horario_pratica = resh_hours("Santo André, SP", "Brasil", -23.63434, -46.53395, "America/Sao_Paulo", 756)
    context = {'ra': horario_pratica['Nascer do sol'].strftime("%H:%M:%S"),
               'ahathoor': horario_pratica['Meio-dia solar'].strftime("%H:%M:%S"),
               'tum': horario_pratica['Pôr do sol'].strftime("%H:%M:%S"),
               'kephera': horario_pratica['Meia-noite solar'].strftime("%H:%M:%S")}
    print(horario_pratica['Meia-noite solar'].strftime("%H:%M:%S"))
    return render(request, 'resh/hours.html', {'context': context})
