from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.split if hasattr(admin.site, 'split') else admin.site.urls),
    path('', include('blog.urls')),  # Conecta las URLs de tu blog en la raíz
]

# Configuración obligatoria para servir archivos multimedia (imágenes) en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

