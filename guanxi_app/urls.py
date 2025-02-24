from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from guanxi_app.core.views import landing_view
from guanxi_app.user.views import login_view, register_view, logout_view


router = routers.SimpleRouter()

apis_urlpatterns = [

]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing_view, name='landing'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('dashboard/', include('guanxi_app.core.urls')),
    path('logout/', logout_view, name='logout'),
    path("__reload__/", include("django_browser_reload.urls")),
] + apis_urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
