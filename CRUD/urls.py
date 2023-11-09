
from django.contrib import admin
from django.urls import path,include

from django.conf.urls.static import static
from django.conf import settings

app_name="Database"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('responsive', include('admin_argon.urls')),
    path('',include('Database.urls')),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
