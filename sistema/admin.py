from django.contrib import admin
from sistema import models

# Register your models here.

# * user register here (optional) *
@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'last_name', 'email', 'active',)
