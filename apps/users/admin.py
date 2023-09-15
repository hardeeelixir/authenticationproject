from django.contrib import admin
from apps.users.models import *

# Register your models here.






class Emailfilter(admin.SimpleListFilter):
    title = 'Email Filter'
    parameter_name = 'user_email'
    def lookups(self, request, model_admin):
        return(
            ('has_email', 'has_email'),
            ('no_email', 'no_email')
        )
    def queryset(self, request, queryset):
        if not self.value():
            return queryset
        if self.value() == 'has_email':
            return queryset.exclude(user__email='')
        if self.value() == 'no_email':
            return queryset.filter(user__email='')

    list_display = ('username', 'firstname', 'lastname', 'email')


class UserAdmin(admin.ModelAdmin):
    list_display = ('bio','user_email')
    list_filter = [Emailfilter]
    def user_email(self, obj):
        return obj.user.email


admin.site.register(UserProfile, UserAdmin)
