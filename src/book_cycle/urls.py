from django.contrib import admin
from django.urls import path, include
from . import views
# for media picture issue
from django.conf import settings
from django.conf.urls.static import static
from . import views
from ..books.views import update 

# ........................................

urlpatterns = [path("admin/", admin.site.urls), path("", include("books.urls")),path("update_server/", views.update, name="update"),]

# for media picture loading issue
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# ........................................
