from django.contrib import admin
from .models import Account, Comment, Preferences
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class AccountAdmin(UserAdmin):
    list_display = ('email','username','date_joined', 'last_login','is_admin','is_staff')
    search_fields = ('email','username')
    readonly_fields = ('date_joined', 'last_login')
    
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    add_fieldsets = (
        (None, {'fields': ('email','username', 'password1', 'password2')}),
        
    )
    

admin.site.register(Account, AccountAdmin)
admin.site.register(Comment)
admin.site.register(Preferences)