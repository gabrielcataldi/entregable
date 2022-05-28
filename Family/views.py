from django.shortcuts import render
from Family.models import Familiar
from unicodedata import name
from multiprocessing import context

# Create your views here.
def familya(request):
    familiar_nuevo = Familiar.object.create(
        nombre = "Graciela",
        edad = 55,
        fecha_nac= '21/03/1967', 
    )
    familiar_nuevo2 = Familiar.object.Create(
       nombre = "Marcelo",
       edad = 58,
       fecha_nac= '26/11/1964',
    )
    familiar_nuevo3 = Familiar.object.Create(
       nombre = "Santiago",
       edad = 24,
       fecha_nac= '20/08/1997',
    )

    context = {'familiar_nuevo': familiar_nuevo, 'familiar_nuevo2': familiar_nuevo2, 'familiar_nuevo3': familiar_nuevo3}
    return render(request, 'family.html')



