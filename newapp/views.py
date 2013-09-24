from datetime import datetime, timedelta
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, loader 
from newapp import models as m
# Create your views here.

def index(request):
	two_days_ago = datetime.utcnow() - timedelta(days=2)
	recent_posts = m.Post.objects.filter(created_at__gt=two_days_ago).all()
	#template = loader.get_template("index.html")
	#template_name = "index.html"
	context = Context({'post_list':recent_posts})
	return render(request, "index.html", context)

def post_detail(request, post_id):
    try:
        post = m.Post.objects.get(pk=post_id)
    except m.Post.DoesNotExist:
        # If no Post has id post_id, we raise an HTTP 404 error.
        raise Http404
    return render(request, 'post/detail.html', {'post': post})
