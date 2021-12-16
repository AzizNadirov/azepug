from django.db import models as m
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from base.models import AbstractComment


class PublishedManager(m.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset().filter(drafted = False)
    

class Tag(m.Model):
    name = m.CharField(max_length=128)

    def __str__(self):
        return str(self.name)


class Post(m.Model):
    title = m.CharField("Başlıq", max_length = 128)
    content = m.TextField("Məzmun")
    author = m.ForeignKey(User, verbose_name= "Müəllif", related_name="posts", on_delete=m.CASCADE)
    date_created = m.DateTimeField("Yaradılma tarixi", default= timezone.now)
    drafted = m.BooleanField(verbose_name="Qaralama", default = False)
    tags = m.ManyToManyField(Tag, verbose_name= "Teqlər",  related_name="posts")

    def get_absolute_url(self):
        return reverse('blog_detail', kwargs = {'pk': self.pk})
        
    #-------------- Managers --------------------------
    objects = m.Manager()
    published = PublishedManager()


    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name, verbose_name_plural = "Post", "Postlar"


class Comment(AbstractComment):
    author = m.ForeignKey(User,verbose_name='müəllif', related_name = 'b_comments', null = True, on_delete=m.SET_NULL)
    post = m.ForeignKey(Post, related_name = 'b_comments', on_delete = m.CASCADE)
   
    def __str__(self):
         return f'Comment to -- " by {self.author} on: {self.created_at}'

