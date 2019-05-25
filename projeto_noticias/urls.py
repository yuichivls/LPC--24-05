from django.contrib import admin
from django.urls import path, include
from app_noticias.views import noticias_detalhes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_noticias.urls')),
    path('noticia/<int:noticia_id>/', noticias_detalhes, name='detalhes'),
    path('conta/', include('django.contrib.auth.urls')),
]
