from django.contrib import admin
from .models import Subject, Video
# Register your models here.

class SubjectAdmin(admin.ModelAdmin):
	pass

admin.site.register(Subject, SubjectAdmin)

class VideoAdmin(admin.ModelAdmin):
	pass

admin.site.register(Video, VideoAdmin)