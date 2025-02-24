from django.urls import path

from staff.views import account_confirm_admin, account_delete_admin, account_update_admin, account_create_admin, account_list_admin

urlpatterns = [
    path('accounts/', account_list_admin, name='account_list_admin'),
    path('accounts/create/', account_create_admin, name='account_create_admin'),
    path('accounts/update/<uuid:pk>/', account_update_admin, name='account_update_admin'),
    path('accounts/delete/<uuid:pk>/', account_delete_admin, name='account_delete_admin'),
    path('accounts/confirm/<uuid:pk>/', account_confirm_admin, name='account_confirm_admin'),
]
