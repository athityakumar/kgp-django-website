from django.contrib import admin
from basicapp.basic.downloads.models import Files



class FilesAdmin(admin.ModelAdmin):
	
		list_display=('filepath','filetype','filesize')
		search_fields=('filetype',)
	
admin.site.register(Files,FilesAdmin)
