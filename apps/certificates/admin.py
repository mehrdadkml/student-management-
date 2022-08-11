from django.contrib import admin
from .models import Certificate
# Register your models here.
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('name',)
   

admin.site.register(Certificate, CertificateAdmin)
