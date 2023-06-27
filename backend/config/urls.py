from django.conf import settings
from django.conf.urls import include, url, re_path
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

from sensors.views import SensorsViewSet

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    url(r'^$', schema_view),
    url(r'^admin/', admin.site.urls),
    url(r'^auth/', include('djoser.urls')),
    url(r'^auth/', include('djoser.urls.jwt')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

router = routers.DefaultRouter()

#Browsable API login
urlpatterns += [
    url(r'^api/auth/', include('rest_framework.urls', namespace='rest_framework')),
    re_path(r'^api/', include(router.urls)),
    path('sensors', SensorsViewSet.as_view({'get': 'getSensorsData'}), name="purple_sensors_view_set"),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
