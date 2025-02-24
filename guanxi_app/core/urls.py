from django.urls import path, include

from guanxi_app.core.views import dashboard_view, profile_view

urlpatterns = [
    path('', dashboard_view, name='dashboard'),
    path('profile/', profile_view, name='profile'),
    path('users/', include('guanxi_app.user.urls')),
    path('admin/', include('guanxi_app.staff.urls')),
    path('profile/', profile_view, name='profile'),
]
