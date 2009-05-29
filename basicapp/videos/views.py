# Create your views here.

from django.shortcuts import render_to_response
from basicapp.videos.models import Video,Tag

def listing(request,template_name='video_list.html'):
	videos_list=Video.objects.all()
	tag_list = Tag.objects.all()
	return render_to_response(template_name,{'videos_list':videos_list,'tag_list':tag_list})

def tag_listing(request,template_name = 'tag_list.html'):
	tag_list = Tag.objects.all()
	return render_to_response(template_name,{'tag_list':tag_list})

def tag_detail(request,tag,template_name = 'tag_detail.html') :
	videos_list=Video.objects.all()
	tag_list = Tag.objects.all()
	return render_to_response(template_name,{'videos_list':videos_list,'tag_list':tag_list,'tag':tag})
