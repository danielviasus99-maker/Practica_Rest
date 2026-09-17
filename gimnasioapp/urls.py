from django.urls import path, include
from django.contrib import admin
from . import views
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from django.conf import settings
from django.conf.urls.static import static
from .views import RutinaViewSet, UsuarioViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'rutinas', RutinaViewSet, basename='rutina')
router.register(r'usuarios', UsuarioViewSet, basename='usuario')


app_name = 'gimnasioapp'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('equipos/', include('maquina.urls')),
    path('', include(router.urls)),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='gimnasioapp:schema'), name='swagger-ui'), #docs/
    path('redoc/', SpectacularRedocView.as_view(url_name='gimnasioapp:schema'), name='redoc'), #redoc/
]