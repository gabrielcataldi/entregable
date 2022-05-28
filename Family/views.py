from django.shortcuts import render
from Family.models import Familiar
from unicodedata import name
from multiprocessing import context

# Create your views here.
def familya(request):
   familiares = Familiar.objects.all()
    
   return render (request, 'family.html', {'familiares': familiares})

