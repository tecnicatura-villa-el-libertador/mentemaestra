from django.conf.urls import url
from django.contrib import admin
from juego.views import jugar, inicio, registrar

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', inicio, name ='inicio'),
    url(r'^registro/(?P<partida_id>[0-9]+)$', registrar, name='registro'),

    url(r'^partida/(?P<partida_id>[0-9]+)$', jugar, name='jugar'),
]
