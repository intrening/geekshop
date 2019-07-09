from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseAdmin
from .models import Account

class AccountInlineAdmin(admin.StackedInline):
    model = Account

class UserAdmin(BaseAdmin):
    inlines = [AccountInlineAdmin]
    # def get_inline_instances(self, *args, **kwargs):
    #     inlines = super (UserAdmin, self).get_inline_instances(*args, **kwargs)
    #     inlines += [AccountInInlineAdmin]
    #     return inlines

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
