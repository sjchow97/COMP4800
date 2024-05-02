# from django.contrib.syndication.views import Feed
# from django.urls import reverse
# from .models import NewsPost

# class NewsPostFeed(Feed):
#     title = "My News"
#     link = "/news/"
#     description = "The latest news from my feed."

#     def items(self):
#         return NewsPost.objects.order_by('-pub_date')[:5]

#     def item_title(self, item):
#         return item.title

#     def item_description(self, item):
#         return item.content

#     def item_link(self, item):
#         return reverse('news_post_detail', args=[item.pk])