from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .models  import *

# Register your models here.
class CustomUserAdmin(UserAdmin):
    
    list_display = (
        'username', 'email', 'first_name', 'last_name', 'is_staff',
        'lab', 
        )

    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
                )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
        ('Additional info', {
            'fields': ('lab', )
        })
    )

    add_fieldsets = (
        (None, {
            'fields': ('username', 'password1', 'password2')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
                )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
        ('Additional info', {
            'fields': ('lab', )
        })
    )


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(specimensreceivedbrticovid19)
admin.site.register(generalbrticovid19)
admin.site.register(Electricoutagebrtivlweekly)
admin.site.register(Reasonsforfailurebrtivlweekly)
admin.site.register(Specimensruncovid19)
admin.site.register(Specimensreceivedcovid19)
admin.site.register(specimensrunbrticovid19)
