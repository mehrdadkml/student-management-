from django.contrib import admin

# Register your models here.

from .models import Lecture
# Register your models here.
class LectureAdmin(admin.ModelAdmin):
    list_display = ('title','date','Lecture_name','date')
    search_fields=('title','Lecture_name')
   

admin.site.register(Lecture, LectureAdmin)

