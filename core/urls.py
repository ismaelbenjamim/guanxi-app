from django.urls import path, include

from core.views import dashboard_view, profile_view

urlpatterns = [
    path('', dashboard_view, name='dashboard'),
    path('profile/', profile_view, name='profile'),
    path('users/', include('user.urls')),
    path('admin/', include('staff.urls')),
    path('profile/', profile_view, name='profile'),
]
