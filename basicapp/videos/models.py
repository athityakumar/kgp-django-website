from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

#This app Embeds videos given a typical choice of video. Eg: YouTube, Google Video etc

class Tag(models.Model):
	
	name = models.TextField(_('Tag Name'),max_length = 50)
	added_time = models.DateTimeField(_('Added Time'),auto_now = True)

	class Meta:
		ordering=('-name',)

	def __unicode__(self):
	        return u'%s' % self.name

class Video(models.Model):
	"""Defines the basic elements of Videos"""
	VIDEOTYPE_CHOICE=(
		('Youtube','Youtube'),
		('Google Video','Google Video'),
	)
	
	video_url_path=models.CharField(_('Video URL'),max_length=400)
	video_embed_path=models.TextField(_('Video Embed Code'))
	video_type=models.CharField(_('Video Type'),max_length=1,choices=VIDEOTYPE_CHOICE)
	video_description=models.TextField(_('Description'))
	added_time=models.DateTimeField(_('Video Embed Stamp'),auto_now=True)
	video_tag = models.ManyToManyField(Tag, blank = True)

	class Meta:
		ordering=('-added_time',)

	def __unicode__(self):
	        return u'%s' % self.video_description




		

