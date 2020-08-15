from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import feedparser

def index(request):
	"""Taking url request as parameter and feeding into feedparser module to store"""
	feed = feedparser.parse(request.GET.get("url", None))

	"""return the parsed object to rss parse views"""
	return render(request, 'rss/parse.html', { 'feed':feed })