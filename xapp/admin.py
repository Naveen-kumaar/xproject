from django.contrib import admin
from xapp.models import register
from xapp.models import patientdetails

# Register your models here.
class RegisterAdmin(admin.ModelAdmin):
    list = ['name','email','mobile','role','Password','C_Password']

admin.site.register(register,RegisterAdmin)

class PatientAdmin(admin.ModelAdmin):
    list =['Date','Name','Age','Gender','Address','Contactno','History','Pain','Duration']
admin.site.register(patientdetails,PatientAdmin)
