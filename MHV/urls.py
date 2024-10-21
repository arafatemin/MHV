from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from publish.views import set_language

# Ana URL kalıpları
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('publish.urls')),
]

# i18n URL kalıpları
urlpatterns = [
    *i18n_patterns(*urlpatterns, prefix_default_language=False),
    path("set_language/<str:language>", set_language, name="set-language"),
]

# Statik ve medya dosyaları URL kalıpları
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
