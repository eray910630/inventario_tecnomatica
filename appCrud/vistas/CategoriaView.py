from rest_framework import serializers,viewsets,generics
from appCrud.models import Inv
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.urlpatterns import format_suffix_patterns


from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import *

from rest_framework.decorators import detail_route, list_route

from django_filters import *
import datetime



# class CategoriaSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Categoria
#         fields = '__all__'
#
# class CategoriaViewSet(viewsets.ModelViewSet):
#     queryset = Categoria.objects.all()
#     serializer_class = CategoriaSerializer
#
# ##########################################################################
#
# class LibroSerializer(serializers.ModelSerializer):
#     categoria = CategoriaSerializer()
#     class Meta:
#         model = Libro
#         fields = '__all__'
#
#
# class LibroViewSet(viewsets.ModelViewSet):
#     serializer_class = LibroSerializer
#     queryset = Libro.objects.all()


class InvSerialize(serializers.ModelSerializer):
    class Meta:
        model = Inv
        fields = '__all__'

# class InvList(generics.ListAPIView):
#     serializer_class  = InvSerialize
#     def get_queryset(self):
#         get_fecha=self.kwargs['fecha']
#         return Inv.objects.filter(fecha=get_fecha)
# y,m,d=(1999,1,1)


# start=datetime.date(2015,6,20)
# end=datetime.date(2015,6,30)
#
# y1,m1,d1=(2015,6,12)
#
# y2,m2,d2=(2015,6,30)
# fecha_start=datetime.date(2015,6,15)
# fecha_end=datetime.date(2015,6,30,)
# Q(fecha=date(2015,6,2)) | Q(fecha=date(2016,6,3)) con esta instruccion lo que hacemos es unir todos los filtros de una consulta con la otra no devuelve un intervalo

# def inventario(request,year_start,month_start,day_start):
#     y1=year_start
#     m1=month_start
#     d1=day_start
#     # y2=year_end
#     # m2=month_end
#     # d2=day_end
#     fecha_start=datetime.date(int(y1),int(m1),int(d1))
#
#     # fecha_end=datetime.date(int(y2),int(m2),int(d2))


class IvnViewSet(generics.ListAPIView):
    serializer_class = InvSerialize
    authentication_classes = (permissions.IsAuthenticatedOrReadOnly,)

    # queryset= Inv.objects.filter(fecha__range=(fecha_start,fecha_end)).order_by("-fecha")
    # @api_view(['GET'])
    # @authentication_classes((SessionAuthentication, BasicAuthentication))
    # @permission_classes((IsAuthenticated,))
    # def example_view(request, format=None):
    #      content = {
    #     'user': unicode(request.user),  # `django.contrib.auth.User` instance.
    #     'auth': unicode(request.auth),  # None
    #   }
    #  return Response(content)

    def get_queryset(self):
        #queryset = Inv.objects.all()
        is_fecha1=False
        is_fecha2=False
        is_productoname=False
        is_calidad=False
        is_volumeninicial=False
        is_volumenactual=False
        is_idtanque=False
        is_idproducto=False
        is_unidadfuncional=False

        if 'fecha1' in self.kwargs and self.kwargs['fecha1'] is not None:
             is_fecha1=True
             if 'fecha2'in self.kwargs and self.kwargs['fecha2'] is not None:
                 is_fecha2=True

        if  'producto'in self.kwargs and self.kwargs['producto'] is not None:
            is_productoname=True

        if 'calidad' in self.kwargs and self.kwargs['calidad'] is not None:
            is_calidad=True
        if 'volumeninicial' in self.kwargs and self.kwargs['volumeninicial'] is not None:
            is_volumeninicial=True
        if 'volumenactual'in self.kwargs and self.kwargs['volumenactual'] is not None:
            is_volumenactual=True
        if 'tanque' in self.kwargs and self.kwargs['tanque'] is not None:
            is_idtanque=True
        if 'idproducto' in self.kwargs and self.kwargs['idproducto'] is not None:
            is_idproducto=True
        if 'funcional' in self.kwargs and self.kwargs['funcional'] is not None:
            is_unidadfuncional=True
        fecha1,fecha2,producto,calidad,volumen_inicial,volumen_actual,tanque,idproducto,funcional_aux=(None,None,None,None,None,None,None,None,None)
        if is_fecha1:
            fecha1=self.kwargs['fecha1']
        if is_fecha2:
                fecha2=self.kwargs['fecha2']
        if is_productoname:
                producto=str(self.kwargs['producto'])
        if is_calidad:
                calidad=str(self.kwargs['calidad'])
        if is_volumeninicial:
                volumen_inicial=float(self.kwargs['volumeninicial'])
        if is_volumenactual:
                volumen_actual=float(self.kwargs['volumenactual'])
        if is_idtanque:
                tanque = str(self.kwargs['tanque'])
        if is_idproducto:
                idproducto = str(self.kwargs['idproducto'])
        if is_unidadfuncional:
                funcional_aux=str(self.kwargs['funcional'])
        if is_fecha1 and is_fecha2 and is_productoname and is_calidad and is_volumeninicial and is_volumenactual and is_idtanque and is_idproducto and is_unidadfuncional:
            date1,date2=fechas(fecha1,fecha2)
            return Inv.objects.filter(unidadfuncional=funcional_aux,fecha__range=(date1,date2),idtanque=tanque,idproducto=idproducto,productoname=producto,volumeninicial=volumen_inicial,volumenactual=volumen_actual,certificadocalidad=calidad).order_by('-fecha')
        elif is_fecha1 and is_productoname and is_calidad and is_volumeninicial and is_volumenactual and is_idtanque and is_idproducto and is_unidadfuncional:
            f1_list = str(fecha1).split()
            date1 = datetime.date(year=int(f1_list[0]), month=int(f1_list[1]), day=int(f1_list[2]))
            return Inv.objects.filter(unidadfuncional=funcional_aux,fecha=date1,idtanque=tanque,idproducto=idproducto,productoname=producto,volumeninicial=volumen_inicial,volumenactual=volumen_actual,certificadocalidad=calidad).order_by('-fecha')
        elif is_fecha1 and is_calidad and is_volumeninicial and is_volumenactual and is_idtanque and is_idproducto and is_unidadfuncional:
                f1_list = str(fecha1).split()
                date1 = datetime.date(year=int(f1_list[0]), month=int(f1_list[1]), day=int(f1_list[2]))
                return Inv.objects.filter(unidadfuncional=funcional_aux,fecha=date1,idtanque=tanque,idproducto=idproducto,volumeninicial=volumen_inicial,volumenactual=volumen_actual,certificadocalidad=calidad).order_by('-fecha')
        elif is_fecha1 and is_volumeninicial and is_volumenactual and is_idtanque and is_idproducto and is_unidadfuncional:
                 f1_list = str(fecha1).split()
                 date1 = datetime.date(year=int(f1_list[0]), month=int(f1_list[1]), day=int(f1_list[2]))
                 return Inv.objects.filter(unidadfuncional=funcional_aux,fecha=date1,idtanque=tanque,idproducto=idproducto,volumeninicial=volumen_inicial,volumenactual=volumen_actual).order_by('-fecha')
        elif is_fecha1 and is_volumenactual and is_idtanque and is_idproducto and is_unidadfuncional:
                 f1_list = str(fecha1).split()
                 date1 = datetime.date(year=int(f1_list[0]), month=int(f1_list[1]), day=int(f1_list[2]))
                 return Inv.objects.filter(unidadfuncional=funcional_aux,fecha=date1,idtanque=tanque,idproducto=idproducto,volumenactual=volumen_actual).order_by('-fecha')
        elif is_fecha1 and is_idtanque and is_idproducto and is_unidadfuncional:
                 f1_list = str(fecha1).split()
                 date1 = datetime.date(year=int(f1_list[0]), month=int(f1_list[1]), day=int(f1_list[2]))
                 return Inv.objects.filter(unidadfuncional=funcional_aux,fecha=date1,idtanque=tanque,idproducto=idproducto).order_by('-fecha')
        elif is_fecha1  and is_idproducto and is_unidadfuncional:
                 f1_list = str(fecha1).split()
                 date1 = datetime.date(year=int(f1_list[0]), month=int(f1_list[1]), day=int(f1_list[2]))
                 return Inv.objects.filter(unidadfuncional=funcional_aux,fecha=date1,idproducto=idproducto).order_by('-fecha')
        elif is_fecha1  and is_unidadfuncional:
                 f1_list = str(fecha1).split()
                 date1 = datetime.date(year=int(f1_list[0]), month=int(f1_list[1]), day=int(f1_list[2]))
                 return Inv.objects.filter(unidadfuncional=funcional_aux,fecha=date1).order_by('-fecha')
        elif is_fecha1 and is_fecha2 and is_productoname:
                date1,date2=fechas(fecha1,fecha2)
                return Inv.objects.filter(fecha__range=(date1,date2),productoname=producto).order_by('-fecha')

        elif is_fecha1 and is_fecha2:
                date1,date2=fechas(fecha1,fecha2)
                return Inv.objects.filter(fecha__range=(date1,date2)).order_by('-fecha')
        # elif is_fecha1:
        #           f1_list = str(fecha1).split()
        #           date1 = datetime.date(year=int(f1_list[0]), month=int(f1_list[1]), day=int(f1_list[2]))
        #           return Inv.objects.filter(fecha=date1).order_by('-fecha')
        elif is_productoname and is_calidad and is_volumeninicial and is_volumenactual and is_idtanque and is_idproducto and is_unidadfuncional:
                return Inv.objects.filter(unidadfuncional=funcional_aux,idtanque=tanque,idproducto=idproducto,productoname=producto,volumeninicial=volumen_inicial,volumenactual=volumen_actual,certificadocalidad=calidad).order_by('-fecha')
        elif is_productoname and is_volumeninicial and is_volumenactual and is_idtanque and is_idproducto and is_unidadfuncional:
                return Inv.objects.filter(unidadfuncional=funcional_aux,idtanque=tanque,idproducto=idproducto,productoname=producto,volumeninicial=volumen_inicial,volumenactual=volumen_actual).order_by('-fecha')
        elif is_productoname  and is_volumenactual and is_idtanque and is_idproducto and is_unidadfuncional:
                return Inv.objects.filter(unidadfuncional=funcional_aux,idtanque=tanque,idproducto=idproducto,productoname=producto,volumenactual=volumen_actual).order_by('-fecha')
        elif is_productoname and is_idtanque and is_idproducto and is_unidadfuncional:
                return Inv.objects.filter(unidadfuncional=funcional_aux,idtanque=tanque,idproducto=idproducto,productoname=producto).order_by('-fecha')
        elif is_productoname  and is_idproducto and is_unidadfuncional:
                return Inv.objects.filter(unidadfuncional=funcional_aux,idproducto=idproducto,productoname=producto).order_by('-fecha')
        elif is_productoname and is_unidadfuncional:
                return Inv.objects.filter(unidadfuncional=funcional_aux,productoname=producto).order_by('-fecha')
        elif is_fecha1 and is_productoname:
                 f1_list = str(fecha1).split()
                 date1 = datetime.date(year=int(f1_list[0]), month=int(f1_list[1]), day=int(f1_list[2]))
                 return Inv.objects.filter(fecha=date1,productoname=producto).order_by('-fecha')
        elif is_calidad and is_volumeninicial and is_volumenactual and is_idtanque and is_idproducto and is_unidadfuncional:
                return Inv.objects.filter(unidadfuncional=funcional_aux,idtanque=tanque,idproducto=idproducto,volumeninicial=volumen_inicial,volumenactual=volumen_actual,certificadocalidad=calidad).order_by('-fecha')
        elif is_calidad and is_volumenactual and is_idtanque and is_idproducto and is_unidadfuncional:
                return Inv.objects.filter(unidadfuncional=funcional_aux,idtanque=tanque,idproducto=idproducto,volumenactual=volumen_actual,certificadocalidad=calidad).order_by('-fecha')
        elif is_calidad  and is_idtanque and is_idproducto and is_unidadfuncional:
                return Inv.objects.filter(unidadfuncional=funcional_aux,idtanque=tanque,idproducto=idproducto,certificadocalidad=calidad).order_by('-fecha')
        elif is_calidad   and is_idproducto and is_unidadfuncional:
                return Inv.objects.filter(unidadfuncional=funcional_aux,idproducto=idproducto,certificadocalidad=calidad).order_by('-fecha')
        elif is_calidad and is_unidadfuncional:
                return Inv.objects.filter(unidadfuncional=funcional_aux,certificadocalidad=calidad).order_by('-fecha')
        elif is_calidad :
                return Inv.objects.filter(certificadocalidad=calidad).order_by('-fecha')
        elif is_volumeninicial and is_volumenactual and is_idtanque and is_idproducto and is_unidadfuncional:
                return Inv.objects.filter(unidadfuncional=funcional_aux,idtanque=tanque,idproducto=idproducto,volumeninicial=volumen_inicial,volumenactual=volumen_actual).order_by('-fecha')
        elif is_volumeninicial and is_idtanque and is_idproducto and is_unidadfuncional:
                return Inv.objects.filter(unidadfuncional=funcional_aux,idtanque=tanque,idproducto=idproducto,volumeninicial=volumen_inicial).order_by('-fecha')
        elif is_volumeninicial  and is_idproducto and is_unidadfuncional:
                return Inv.objects.filter(unidadfuncional=funcional_aux,idproducto=idproducto,volumeninicial=volumen_inicial).order_by('-fecha')
        elif is_volumeninicial  and is_unidadfuncional:
                return Inv.objects.filter(unidadfuncional=funcional_aux,volumeninicial=volumen_inicial).order_by('-fecha')
        elif is_volumeninicial :
                return Inv.objects.filter(volumeninicial=volumen_inicial).order_by('-fecha')
        elif is_volumenactual and is_idtanque and is_idproducto and is_unidadfuncional:
                return Inv.objects.filter(unidadfuncional=funcional_aux,idtanque=tanque,idproducto=idproducto,volumenactual=volumen_actual).order_by('-fecha')
        elif is_volumenactual and is_idproducto and is_unidadfuncional:
                return Inv.objects.filter(unidadfuncional=funcional_aux,idproducto=idproducto,volumenactual=volumen_actual).order_by('-fecha')
        elif is_volumenactual  and is_unidadfuncional:
                return Inv.objects.filter(unidadfuncional=funcional_aux,volumenactual=volumen_actual).order_by('-fecha')
        elif is_volumenactual :
                return Inv.objects.filter(volumenactual=volumen_actual).order_by('-fecha')
        elif is_idtanque and is_idproducto and is_unidadfuncional:
                return Inv.objects.filter(unidadfuncional=funcional_aux,idtanque=tanque,idproducto=idproducto).order_by('-fecha')
        elif is_idtanque  and is_unidadfuncional:
                return Inv.objects.filter(unidadfuncional=funcional_aux,idtanque=tanque).order_by('-fecha')
        elif is_idtanque :
                return Inv.objects.filter(idtanque=tanque).order_by('-fecha')
        elif is_idproducto and is_unidadfuncional:
                return Inv.objects.filter(unidadfuncional=funcional_aux,idproducto=idproducto).order_by('-fecha')
        elif is_idproducto :
                return Inv.objects.filter(idproducto=idproducto).order_by('-fecha')
        elif is_unidadfuncional:
                return Inv.objects.filter(unidadfuncional=funcional_aux).order_by('-fecha')
        elif is_fecha1 and is_fecha2 and is_productoname:
                date1,date2=fechas(fecha1,fecha2)
                return Inv.objects.filter(fecha__range=(date1,date2),productoname=producto)
        elif is_fecha1 and is_idproducto:
                 f1_list = str(fecha1).split()
                 date1 = datetime.date(year=int(f1_list[0]), month=int(f1_list[1]), day=int(f1_list[2]))
                 return Inv.objects.filter(fecha=date1,idproducto=idproducto)
        elif is_fecha1 and is_fecha2 and is_idtanque:
            date1,date2=fechas(fecha1,fecha2)
            return Inv.objects.filter(fecha__range=(date1,date2),idtanque=tanque).order_by('-fecha')
        return Inv.objects.all()







def fechas(fecha1,fecha2):
    f1_list = str(fecha1).split()
    f2_list = str(fecha2).split()
    date1 = datetime.date(year=int(f1_list[0]), month=int(f1_list[1]), day=int(f1_list[2]))
    date2 = datetime.date(year=int(f2_list[0]), month=int(f2_list[1]), day=int(f2_list[2]))
    return date1,date2























    #queryset=Inv.objects.filter(fecha=fecha_start)
    # def get_queryset(self):
    #     if self.request.method=='GET':
    #         self.queryset=Inv.objects.filter(fecha=datetime.date(int(self.request.data[0]),int(self.request.data[1]),int(self.request.data[2]))).order_by("-fecha")
    #     return self.queryset









    # def set_password(self, request, pk=None):
    #     user = self.get_object()
    #     serializer = InvSerialize(fecha=request.data)
    #     if serializer.is_valid():
    #         user.set_password(serializer.data['password'])
    #         user.save()
    #         return Response({'status': 'password set'})
    #     else:
    #         return Response(serializer.errors,
    #                         )

    # queryset= Inv.objects.filter(fecha__range=(fecha_start,fecha_end)).order_by("-fecha")   #esto ordena de menor a mayor si le pongo el menos delante de la fecha ordena de mayor a menor es a conveniencia

    # queryset = filter(intervalo(),)







