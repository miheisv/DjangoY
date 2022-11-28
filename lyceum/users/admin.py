from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from users.models import Profile, Registration


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False


class UserAdmin(BaseUserAdmin):
    inlines = (
        ProfileInline,
    )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Registration)
