from django.conf.urls import url, include
#from registro.views import index, RegistroList
from django.views.generic import ListView, TemplateView
from.views import indexRegistro, registro_view, RegistroList

urlpatterns = [
url(r'^$', indexRegistro, name='index'),
url(r'^registros$', registro_view, name='index_compra'),
url(r'^listarcompra$', RegistroList.as_view(), name='registro_listar'),


] 