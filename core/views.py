from django import urls
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.views.generic.base import RedirectView
from django.contrib import messages
from core.models import Evento

# def index(request):
#     return redirect('/agenda')

def login_page(request):
    return render(request, 'login.html')

def logout_page(request):
    
    logout(request)

    return redirect("/login")

def login_submit(request):

    if request.POST:

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
        else:
            messages.error(request,"Usuário ou senha inválido")

    
    return redirect("/")



# Create your views here.
@login_required(login_url='/login')
def lista_eventos(request):
    
    usuario = request.user
    eventos = Evento.objects.filter(usuario=usuario)
    # eventos = Evento.objects.all()
    dados = {'eventos': eventos}
    
    return render(request,'agenda.html', dados)