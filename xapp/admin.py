from django.contrib import admin
from xapp.models import register

# Register your models here.
class RegisterAdmin(admin.ModelAdmin):
    list = ['name','email','mobile','role','Password','C_Password']

admin.site.register(register,RegisterAdmin)