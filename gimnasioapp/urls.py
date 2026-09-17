from django.urls import path, include
from django.contrib import admin
from . import views
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from django.conf import settings
from django.conf.urls.static import static
from .views import RutinaViewSet, UsuarioViewSet, GimnasioViewSet, EjercicioViewSet, DetalleRutinaViewSet, SesionEntrenamientoViewSet
from rest_framework.routers import DefaultRouter

app_name = 'gimnasioapp'

router = DefaultRouter()
router.register(r'gimnasios', views.GimnasioViewSet)
router.register(r'usuarios', views.UsuarioViewSet)
router.register(r'ejercicios', views.EjercicioViewSet)
router.register(r'rutinas', views.RutinaViewSet)
router.register(r'detalles-rutina', views.DetalleRutinaViewSet)
router.register(r'sesiones-entrenamiento', views.SesionEntrenamientoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('equipos/', include('maquina.urls')),
    path('api/', include(router.urls)),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='gimnasioapp:schema'), name='swagger-ui'), #docs/
    path('redoc/', SpectacularRedocView.as_view(url_name='gimnasioapp:schema'), name='redoc'), #redoc/
]
