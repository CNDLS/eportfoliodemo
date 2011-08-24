from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as RealUserAdmin

from library.models import LibraryState
from profiles.models import UserProfile

class UserProfileInline(admin.StackedInline):
    model = UserProfile

class UserAdmin(RealUserAdmin):
    inlines = [ UserProfileInline ]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(LibraryState)