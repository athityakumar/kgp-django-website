# Create your views here.
from django.shortcuts import render_to_response
from basicapp.basic.downloads.models import Files


def listing(request,template_name='download_listing.html'):
	file_list=Files.objects.all()
	return render_to_response(template_name,{'file_list':file_list , 'user' : request.user,})
