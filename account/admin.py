from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from django.utils.translation import ugettext_lazy as _

from .forms import UserCreationForm, UserChangeForm
from .models import User


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('id', 'name', 'email', 'department', 'is_superuser',)
    list_filter = ('is_superuser',)
    fieldsets = (
        (None, {'fields': ('id', 'password')}),
        (_('Personal info'), {'fields': ('name', 'email', 'department')}),
        (_('Permissions'), {'fields': ('is_superuser',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('id', 'name', 'email', 'department', 'password1', 'password2')}
         ),
    )
    search_fields = ('email', 'name', 'id')
    ordering = ('name',)
    filter_horizontal = ()

admin.site.register(User, UserAdmin)
admin.site.unregister(Group)