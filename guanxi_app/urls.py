from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from core.views import landing_view, dashboard_view
from user.api.viewsets import AccountBindAPIView
from user.views import login_view, register_view, logout_view


router = routers.SimpleRouter()

apis_urlpatterns = [
    path('api/accounts/bind', AccountBindAPIView.as_view(), name="create-account"),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing_view, name='landing'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('dashboard/', include('core.urls')),
    path('logout/', logout_view, name='logout'),
    path("__reload__/", include("django_browser_reload.urls")),
] + apis_urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
