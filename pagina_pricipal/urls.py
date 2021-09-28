from django.urls import path
from .views import  inicioView, programacaoView, apoiadoresView, palestrasView, workshopsView, diasPalestrasView


#Have to configure to all paths use the slug

urlpatterns = [

    #site urls
    path('', inicioView, name = 'inicio'),
    
    path('programacao/', programacaoView, name = 'programacao'),
    
    path('apoiadores/', apoiadoresView, name = 'apoiadores'),
    path('dias-de-palestras/', diasPalestrasView, name = 'dias_palestras'),
    path('palestras/<slug:slug1>/', palestrasView, name = 'palestras'),
    path('workshops/', workshopsView, name = 'workshops'),

    

    
    
    

    #Testes
    #path('teste/', teste1, name='teste')

    
]


