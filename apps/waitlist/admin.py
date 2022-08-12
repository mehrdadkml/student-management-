from tabnanny import verbose
from django.contrib import admin


from .models import WaitListEntry
# Register your models here.
class WaitlistAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name',)
    search_fields=('first_name','last_name',)
   

admin.site.register(WaitListEntry, WaitlistAdmin)

class Meta:
    verbose_name_plural='waitlist entries'