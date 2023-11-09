from django.contrib import admin

from .models import Students,Sliders

from django.contrib.auth.admin import UserAdmin

from Database.form import CustomUserCreationForm,CustomUserChangeForm

from Database.models import CustomUser

# Register your models here.

admin.site.register(Students)

admin.site.register(Sliders)

admin.site.site_header='STUDENTS ADMIN PAGE'

class CustomUserAdmin(UserAdmin):
    add_form=CustomUserCreationForm
    form=CustomUserChangeForm


admin.site.register(CustomUser,CustomUserAdmin)

