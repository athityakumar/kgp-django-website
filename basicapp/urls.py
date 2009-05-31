from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('django.views.generic.simple',
    # Example:
    # (r'^basicapp/', include('basicapp.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #	(r'^blog/', include('basicapp.basic.blog.urls')),
    #	(r'^admin/(.*)', admin.site.root),	
    #	(r'^comments/', include('basicapp.basic.comments.urls')),	
    #	(r'^downloads/',include('basicapp.basic.downloads.urls')),
    #	(r'^forum/', include('basicapp.forum.urls')),	
    #	(r'^account/', include('django_authopenid.urls')),
    #	(r'^$','redirect_to', {'url': '/account/signin/complete'}), 
    #	(r'^cab/',include('basicapp.cab.urls')),
    #	(r'^videos/',include('basicapp.videos.urls')),
    #	(r'^accounts/login/','redirect_to',{'url':'/account/signin/complete'}),
    #	(r'^wiki/',include('basicapp.wiki.urls')),
        
	(r'^admin/(.*)', admin.site.root),
        (r'^blog/', include('basicapp.basic.blog.urls')),
	(r'^comments/', include('basicapp.basic.comments.urls')),	
	(r'^downloads/',include('basicapp.basic.downloads.urls')),
	(r'^forum/', include('basicapp.forum.urls')),	
	(r'^account/', include('django_authopenid.urls')),
	(r'^$','redirect_to', {'url': '/kgp/blog/'}),
	(r'^cab/',include('basicapp.cab.urls')),
	(r'^videos/',include('basicapp.videos.urls')),
	(r'^accounts/login/','redirect_to',{'url':'/kgp/account/signin/complete'}),
	(r'^wiki/',include('basicapp.wiki.urls')),
)








