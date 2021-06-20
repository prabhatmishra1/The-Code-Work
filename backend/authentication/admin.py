from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . models import User, Code
from . forms import UserAdminChangeForm, UserAdminCreationForm
# Register your models here.


''' =============================================================================
    Description: Customuser Admin Interface.    
    Author:Prabhat Mishra
    ==============================================================================
'''


class CustomUserAdmin(UserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    model = User

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('id', 'email', 'first_name')
    list_filter = ('email',)
    fieldsets = (
        ("Authentication", {'fields': ('email', 'password',)}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'mobile')}),
        ('Important Dates', {'fields': ('date_joined', 'last_login',)}),
        ('Admin Permissions', {
         'fields': ('is_active', 'is_staff', 'is_superuser',)}),

    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.

    add_fieldsets = (
        ("Authentication", {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2',),
        }),
    )
    search_fields = ('email',)
    ordering = ('-id',)
    filter_horizontal = ()


admin.site.site_header = 'Test'
admin.site.register(User, CustomUserAdmin)
admin.site.register(Code)
