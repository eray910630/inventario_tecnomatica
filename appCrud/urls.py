from django.conf.urls import include, url
from rest_framework import routers

# from appCrud.vistas.CategoriaView import CategoriaViewSet, LibroViewSet
from appCrud.vistas.CategoriaView import IvnViewSet, fechas
import Crud.settings as seting
from appCrud import vistas
from appCrud.vistas import CategoriaView


router = routers.DefaultRouter()
# router.register(r'categorias', CategoriaViewSet)
# router.register(r'Libros', LibroViewSet)
# router.register(r'Venta', VentaViewSet)
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

     # url(r'^Inv/(?P<fecha1>\d{4} \d{1,2} \d{1,2})/(?P<fecha2>\d{4} \d{1,2} \d{1,2})/$', IvnViewSet.as_view()),

      url(r'^Inv/?(?P<fecha1>\d{4} \d{1,2} \d{1,2})?/?(?P<fecha2>\d{4} \d{1,2} \d{1,2})?/?(?P<producto>[a-zA-Z][\w\.\s]+)?/?(?P<calidad>[\d]+)?/?(?P<volumeninicial>[\d\.]+)?/?(?P<volumenactual>[\d\.]+)?/?(?P<tanque>[\w\.]+)?/?(?P<idproducto>[\d]+)?/?(?P<funcional>[\w\.]+)?/$', IvnViewSet.as_view()),

     # url(r'^Inv/(?P<producto>[A-Za-z0-9\s\.]+)/$', IvnViewSet.as_view()),
    # url(r'^Inv/(?P<producto>[\w\W]+)/$', IvnViewSet.as_view()),


       # url(r'^Inv/?(?P<fecha1>\d{4} \d{1,2} \d{1,2})?/?(?P<fecha2>\d{4} \d{1,2} \d{1,2})?/?(?P<producto>[\w\W\d]+)?/?(?P<temperatura>[\w\W\d]+)?/?(?P<densidad>[\w\W\d]+)?/?(?P<calidad>[\w\W\d]+)?/?(?P<volumeninicial>[\w\W\d]+)?/?(?P<volumenactual>[\w\W\d]+)?/?(?P<tanque>[\w\W\d]+)?/?(?P<idproducto>[\w\W\d]+)?/?(?P<funcional>[\w\W\d]+)?/$', IvnViewSet.as_view()),






   # url(r'^Inv/(?P<producto>[\w\W\d]+)/(?P<temperatura>[\w\W]+)/$', IvnViewSet.as_view()),



        # url(r'^Inv/(?P<producto>[\w\W]+)/?(?P<fecha1>\d{4} \d{1,2} \d{1,2})?/?(?P<fecha2>\d{4} \d{1,2} \d{1,2})?/$', IvnViewSet.as_view()),

     # url(r'^Inv/(?P<producto>[\w\W]+)/(?P<fecha1>\d{4} \d{1,2} \d{1,2})/(?P<fecha2>\d{4} \d{1,2} \d{1,2})/$', IvnViewSet.as_view()),
    # url(r'^fecha/(?P<fecha1>\w+)/(?P<fecha2>\w)/$', fechas)

]

# # if seting.DEBUG:
# #     urlpatterns += [
# #         url (r'^debuginfo/$',),
#     ]