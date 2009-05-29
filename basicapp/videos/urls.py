from django.conf.urls.defaults import *

urlpatterns = patterns('',
	(r'^$','basicapp.videos.views.listing'),
	(r'^tags/(?P<tag>\w+)','basicapp.videos.views.tag_detail'),	
	(r'^tags/$','basicapp.videos.views.tag_listing'),
)
