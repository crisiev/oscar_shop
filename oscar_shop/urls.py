from django.contrib import admin
from django.urls import path, include
from oscar.app import application
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', application.urls),  # Usa directamente las URLs de Oscar
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
