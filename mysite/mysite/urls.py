from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
import debug_toolbar

from mysite import settings

urlpatterns = [
    path('', include('Goods.urls')),
    path('admin/', admin.site.urls),

]
if settings.DEBUG:
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
