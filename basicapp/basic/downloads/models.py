from django.db import models
from django.utils.translation import ugettext_lazy as _
import os

# Create your models here.

FILETYPE_CHOICE=(
	('Audio/Video','Audio/Video'),
	('Text/Word','Text/Word'),
	('source','Source Archives'),
	('Binary','All other files go here!'),
) 
	

class Files(models.Model):
	
	"""Downloads area model"""
	

	filepath = models.FilePathField(_('Choose File'),path="/home/sumit/Downloads/")
	filedescription = models.CharField(_('File Description'),max_length=100)
	filetype = models.CharField(_('File Type'),max_length=1,choices=FILETYPE_CHOICE)
	filesize=models.FloatField(_('Size(MB)'),null=True,blank=True, editable=False)
	fileuploadtime = models.DateTimeField(_('File Upload Time'))
	
	def __unicode__(self):
		return self.filepath
		
	class Admin:
		list_display  = ('filepath','filesize','fileuploaddate','fileuploadtime')
		list_filter   = ('fileuploaddate')
		
	def save(self, force_insert=False, force_update=False):
		"""Update the size field and save the record"""
		
		if self.filepath:		
			self.filesize=os.path.getsize(self.filepath)/(1024.0*1024.0)
			super(Files, self).save(force_insert,force_update) 

