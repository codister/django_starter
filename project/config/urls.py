from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    url(r'^secret/', include(admin.site.urls)),
    url(r'^', include('starter_app.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

