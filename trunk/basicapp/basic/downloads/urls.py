from django.conf.urls.defaults import *

urlpatterns = patterns('',
	(r'^$','basicapp.basic.downloads.views.listing'),
	(r'^files/(?P<path>.*)$','django.views.static.serve',
		{'document_root': '/'}),
)
