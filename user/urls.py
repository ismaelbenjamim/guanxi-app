from django.urls import path

from user.views import account_list, account_create, account_update, \
    account_delete, account_confirm

urlpatterns = [
    path('accounts/', account_list, name='account_list'),
    path('accounts/create/', account_create, name='account_create'),
    # path('accounts/update/<uuid:pk>/', account_update, name='account_update'),
    path('accounts/delete/<uuid:pk>/', account_delete, name='account_delete'),
    path('accounts/confirm/<uuid:pk>/', account_confirm, name='account_confirm'),
]
