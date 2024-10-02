from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('estilos/', include('estilo.urls')),
    path('musicas', include('musicas.urls'))
]
