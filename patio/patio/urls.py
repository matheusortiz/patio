from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contas/', include('usuarios.urls'), name='login' ),
    path('contas/', include('django.contrib.auth.urls')),
    path('', include('remocoes.urls'), name='home' ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
