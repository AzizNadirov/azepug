from django.db import models as m
from django.conf import settings
from django.urls import reverse
from base.models import AbstractComment, AbstractPost
from taggit.managers import TaggableManager





class PublishedManager(m.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset().filter(drafted = False)
    


class Post(AbstractPost):
    author = m.ForeignKey(settings.AUTH_USER_MODEL, verbose_name= "Müəllif", related_name="posts", on_delete=m.CASCADE)
    tags = TaggableManager()
    likes = m.ManyToManyField(settings.AUTH_USER_MODEL, related_name="liked_blog")
    like_count = m.IntegerField(default=0)
    objects = m.Manager()
    published = PublishedManager()

    def get_absolute_url(self):
        return reverse('blog_detail', kwargs = {'pk': self.pk})


    def __str__(self):
        return self.title


class Comment(AbstractComment):
    author = m.ForeignKey(settings.AUTH_USER_MODEL,verbose_name='müəllif', related_name = 'b_comments', null = True, on_delete=m.SET_NULL)
    post = m.ForeignKey(Post, related_name = 'b_comments', on_delete = m.CASCADE)
   
    def __str__(self):
         return f'Comment to -- " by {self.author} on: {self.created_at}'

