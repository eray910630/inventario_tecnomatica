from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView



class index(TemplateView):
     template_name = 'base.html'


#class principal(TemplateView):
    #template_name = 'principal.html'

#class test1(TemplateView):
    #template_name = 'test1.html'

#class categorias(TemplateView):
    #template_name = 'categorias.html'


class Home(TemplateView):
    template_name = 'static/views/principal.html'





