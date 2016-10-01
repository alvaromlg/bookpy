from django.conf.urls import include, url
from django.contrib import admin

# TODO serving static files for dev env
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('finder.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^v1/api/', include('library.urls', namespace='v1')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
