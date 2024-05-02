from django.shortcuts import render
from django.http import HttpResponse
import feedparser


def index(request):
    feeds = feedparser.parse("https://johnsmallman.wordpress.com/author/johnsmallman/feed/")
    feed_entries = []
    for entry in feeds.entries:
        feed_entry = {
            'title': entry.title,
            'link': entry.link,
            # 'pubDate': entry.pubDate,
            'description': entry.description,
            
            # Add more attributes as needed
        }
        feed_entries.append(feed_entry)
    return render(request, 'index.html', {'feed_entries': feed_entries})