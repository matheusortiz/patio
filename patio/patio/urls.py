from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contas/', include('usuarios.urls', namespace='usuarios')),
    path('contas/', include('django.contrib.auth.urls')),
    path('', include('remocoes.urls', namespace='remocoes')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
