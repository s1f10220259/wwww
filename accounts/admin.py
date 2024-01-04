# Register your models here.
from django.contrib import admin
from django.contrib.auth.models import Group

from accounts.models import User

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

class UserAdmin(BaseUserAdmin):
    # ユーザーモデルのカスタムフィールドをここで定義されたフィールドセットに追加します
    fieldsets = (
        (None, {'fields': ('email', 'password', 'account_id', 'first_name', 'last_name', 'birth_date')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login', 'created_at', 'updated_at')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('account_id', 'email', 'password1', 'password2'),
        }),
    )
    list_display = ('account_id', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('account_id', 'email', 'first_name', 'last_name')
    ordering = ('account_id',)



admin.site.register(User, UserAdmin)  # Userモデルを登録
admin.site.unregister(Group)  # Groupモデルは不要のため非表示にします
