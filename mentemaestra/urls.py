from django.conf.urls import url
from django.contrib import admin
from juego.views import jugar, inicio, registrar

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', inicio, name ='inicio'),
    url(r'^registro/(?P<id>[a-zA-Z]+)$', registrar, name='privado'),
    url(r'^registro/(?P<id>[0-9]+)$', registrar, name='registro'),

    url(r'^partida/(?P<id>[0-9]+)$', jugar, name='jugar'),
    url(r'^partida/(?P<id>[a-zA-Z]+)$', jugar, name='jugar'),

]
