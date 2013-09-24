from datetime import datetime, timedelta
from django.http import HttpResponse
from django.template import Context, loader 
from newapp import models as m
# Create your views here.

def index(request):
	two_days_ago = datetime.utcnow() - timedelta(days=2)
	recent_posts = m.Post.objects.filter(created_at__gt=two_days_ago).all()
	template = loader.get_template("index.html")
	#template_name = "index.html"
	context = Context({'post_list':recent_posts})
	return HttpResponse(template.render(context))
