from django.contrib import admin

from .models import Skills,About,Certificate,Education,Works

class MainAdmin(admin.ModelAdmin):
    list_display=("skill","degree","color")




admin.site.register(Skills,MainAdmin),
admin.site.register(About),
admin.site.register(Certificate),
admin.site.register(Education),
admin.site.register(Works),