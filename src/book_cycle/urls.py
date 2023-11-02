from django.contrib import admin
from django.urls import path, include

#for media picture issue
from django.conf import settings
from django.conf.urls.static import static
#........................................

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('books.urls'))
]

# for media picture loading issue
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#........................................