import json

from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def landing_view(request):
    return render(request, 'landing.html')


@login_required(login_url='login')
def dashboard_view(request):
    user = request.user

    context = {
        "followers_added": "602",
        "total_accounts": 20,
        "total_orders": "500",
        "lastest_orders": "20",
        "followers_labels": json.dumps([
            "a", "b"
        ]),
        "followers_data": json.dumps([
            "a", "b"
        ]),
        "engagement_labels": json.dumps([
            "a", "b"
        ]),
        "engagement_data": json.dumps([
            "a", "b"
        ])
    }

    return render(request, 'dashboard/dashboard.html', context)


@login_required(login_url='login')
def profile_view(request):
    return render(request, 'dashboard/profile.html')
