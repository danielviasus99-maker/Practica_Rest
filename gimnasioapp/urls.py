from django.urls import path, include
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from . import views

router = DefaultRouter()
router.register(r'gimnasios', views.GimnasioViewSet)
router.register(r'usuarios', views.UsuarioViewSet)
router.register(r'ejercicios', views.EjercicioViewSet)
router.register(r'rutinas', views.RutinaViewSet)
router.register(r'detalles-rutina', views.DetalleRutinaViewSet)
router.register(r'sesiones-entrenamiento', views.SesionEntrenamientoViewSet)

urlpatterns = [
    path('', views.home, name='home'),
    path('api/', include(router.urls)),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('equipos/', include('maquina.urls')),
] 