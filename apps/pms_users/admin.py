from datetime import date
from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from apps.pms_users.models import *
# from django_admin_filter import MultiChoice

# Register your models here.



@admin.register(PmsData)
class PmsAdmin(admin.ModelAdmin):
    list_display = ('username', 'firstname', 'lastname', 'email')
    search_fields = ('username', 'firstname')
    ordering = ('username',)
    list_filter = ['firstname', 'lastname']

# @admin.register(PmsData)
# class PmsAdminm(admin.SimpleListFilter):
#     title = "_username-list"

# class DecadeBornListFilter(admin.SimpleListFilter):
#         title = _("decade_born")
#
#         parameter_name = "decade"
#
#         def lookups(self, request, model_admin):
#             return[
#                 ("80s", _("in eighties")),
#                 ("90s", _("in ninties")),
#             ]
#
#         def queryset(self, request, queryset):
#             if self.value() == "80s":
#                 return queryset.filter(
#                     birthday__gte=date(1980, 1, 1),
#                     birthday__lte=date(1989, 12, 31),
#                 )
#             if self.value == "90s":
#                 return queryset.filter(
#                         birthday__gte = date(1990, 1, 1),
#                         birthday__lte = date(1999, 12, 31)
#                     )


# admin.site.register(PmsData, DecadeBornListFilter)
