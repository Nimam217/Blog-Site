from django.contrib.syndication.views import Feed
from django.urls import reverse
from .models import Post


class LatestEntriesFeed(Feed):
    title = "Blog feed"
    link = "/rss/feed/"
    description = "Posts Are Here."

    def items(self):
        return Post.objects.all()

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content[:75]

