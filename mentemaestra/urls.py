from django.conf.urls import url
from django.contrib import admin
from juego.views import jugar

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^comenzar.html/', jugar),
]
