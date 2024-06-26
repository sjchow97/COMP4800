from django.shortcuts import render
from django.http import HttpResponse
import feedparser


def index(request):
    # feeds = feedparser.parse("https://johnsmallman.wordpress.com/author/johnsmallman/feed/")
    feeds = feedparser.parse("https://www.yellowknife.ca/Modules/News/en//rss")
    feed_entries = []
    for entry in feeds.entries:
        feed_entry = {
            'title': entry.title,
            'link': entry.link,
            'published': entry.published,
            'description': entry.description,
            
            # Add more attributes as needed
        }
        feed_entries.append(feed_entry)
        # print(entry)
    return render(request, 'index.html', {'feed_entries': feed_entries})