from django.shortcuts import render,redirect
from core.models import Evento

# def index(request):
#     return redirect('/agenda')


# Create your views here.
def lista_eventos(request):
    
    # usuario = request.user
    # eventos = Evento.objects.filter(usuario=usuario)
    eventos = Evento.objects.all()
    dados = {'eventos': eventos}
    
    return render(request,'agenda.html', dados)