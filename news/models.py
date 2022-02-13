from django.db import models
from django.conf import settings

from django.urls.base import reverse
from taggit.managers import TaggableManager
from base.models import AbstractComment,AbstractPost



class Comment(AbstractComment):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name='müəllif', related_name = 'n_comments', null = True, on_delete=models.SET_NULL)
    news = models.ForeignKey('News', related_name = 'n_comments', on_delete = models.CASCADE)

    def __str__(self):
         return f'Comment to -- " by {self.author} on: {self.created_at}'

class News(AbstractPost):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name = "news")
    image = models.ImageField()
    tags = TaggableManager()
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="liked_news")
    like_count = models.IntegerField(default=0)

    def __str__(self):
        return f"News: {self.title} : {self.author}"
    
    def get_absolute_url(self):
        return reverse("news_detail", kwargs={"pk": self.pk})
