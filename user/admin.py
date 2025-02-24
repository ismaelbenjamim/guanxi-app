from django.contrib import admin

from user.models import User, Account, Follower

admin.site.register(User)
admin.site.register(Account)
admin.site.register(Follower)
