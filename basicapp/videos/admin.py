from django.contrib import admin
from basicapp.videos.models import Video,Tag

class VideoAdmin(admin.ModelAdmin):
		list_display=('video_url_path','video_type','added_time')
		list_filter=('video_type','added_time')
		search_fields=('video_path',)
admin.site.register(Video,VideoAdmin)

class TagAdmin(admin.ModelAdmin):
		list_display = ('name','added_time')


admin.site.register(Tag,TagAdmin)
