from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from appCrud import views, urls
from appCrud.vistas import CategoriaView



urlpatterns = [
    # Examples:
    # url(r'^$', 'Crud.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(urls)),
    url(r'^$', views.index.as_view()),
    #url(r'^principal/', views.principal.as_view()),
   # url(r'^test1/', views.test1.as_view()),
   # url(r'^categorias/', views.categorias.as_view()),
    #url(r'^/', views.Home.as_view()),
    # url(r'^api/Inv/(\d{4})/(\d{2})/(\d{2})-(\d{4})/(\d{2})/(\d{2})/$', CategoriaView.inventario),
    #  url(r'^Inv/((\d{4})/(\d{2})/(\d{2})-(\d{4})/(\d{2})/(\d{2}))/$', CategoriaView.inventario),


]
