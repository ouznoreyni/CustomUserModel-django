from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import UserProfile
from .forms import UserCreationForm, UserChangeForm
# Register your models here.
#admin.site.register(UserProfile)

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff',)
    
    fieldsets = (
        (None, {'fields': ('email', 'password' ),}),
        ('Personal info', {'fields': ('first_name', 'last_name'),}),
        ('Permissions', {'fields': ('is_active', 'is_staff',)}),
    )

    add_fieldsets = (
        (None, {
            'classes':('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2')
            }
        ),
    )

    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(UserProfile, UserAdmin)
admin.site.unregister(Group)