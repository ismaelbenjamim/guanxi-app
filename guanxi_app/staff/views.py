from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404


def superuser_required(user):
    return user.is_superuser
