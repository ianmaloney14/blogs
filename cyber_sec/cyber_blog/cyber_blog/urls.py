from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog_app.urls')),
    path('admin_login/', include('django.contrib.auth.urls')),
    path('admin_login/', include('admin_login.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
