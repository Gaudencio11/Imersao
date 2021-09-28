#Não usar esse código para esacabilidade de um possível site de eventos
#Usar código da sapiens principal

from .models import Palestra, Workshop
from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail

def inicioView(request): 
     

    if  Palestra.objects.all()[0] :
        palestra = Palestra.objects.all()[0]
        link = palestra.link
    else:
        link = "https://www.youtube.com/"


    return render(request, 'homepage.html', {"link":link, })


def programacaoView(request):


    return render(request, 'programacao.html', {})


def apoiadoresView(request):

    return render(request, 'apoiadores.html', {})


#slug1 é a palestra específica
def palestrasView(request, slug1):

    return render(request, 'palestras.html', {"dia":slug1})


def diasPalestrasView(request):

    return render(request, 'days.html', {})




#slug1 é o workshop que a pessoa clickou
def workshopsView(request):

    objetos = Workshop.objects.all()
    lista_links=[]

    for item in objetos:
        lista_links.append(item.link)

    backend = lista_links[0] 
    frontend = lista_links[1]
    mobile = lista_links[2]
    git = lista_links[3]
    gp = lista_links[4]
    requisitos = lista_links[5]
    testes = lista_links[6]
    devops = lista_links[7]
    bd = lista_links[8]
    jogos = lista_links[9]
    deploy = lista_links[10]
  


    return render(request, 'workshops.html', {"backend":backend,"frontend":frontend, "mobile":mobile,
"git":git, "gp":gp, "requisitos":requisitos, "testes":testes, "devops":devops, "bd":bd, "jogos":jogos
,"deploy":deploy, 'lista_links':lista_links})





"""def teste1(request):

    

    if not request.user.is_superuser: 
        user_name = request.user.first_name.split()
        user_name = user_name[0]
    else:
        user_name = request.user.username

    event = Event.objects.all()[0]
    rooms = Room.objects.all() 


    return render(request, 'historia.html', {'event': event, 'rooms':rooms, "user_name":user_name})"""
    


