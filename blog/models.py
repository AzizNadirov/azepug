from django.db import models as m
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class PublishedManager(m.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset().filter(status = 'Published')

class Tags(m.Model):
    tag = m.CharField('tag',max_length=20)
    

class Category(m.Model):
    name_of_category = m.CharField('Kateqoriya', max_length= 30)

    def __str__(self):
        return self.name_of_category
    class Meta:
        verbose_name = "Kateqoriya"
        verbose_name_plural = "Kateqoriyalar"

    class Meta:
        verbose_name = 'Kateqoriya'
        verbose_name_plural = 'Kateqoriyalar'

class Post(m.Model):
    category = m.ForeignKey(Category, null =True, on_delete=m.SET_NULL)
    title = m.CharField("Başlıq", max_length=20)
    content = m.TextField()
    author = m.ForeignKey(User, on_delete=m.CASCADE)
    date_created = m.DateTimeField(default= timezone.now)
    STATUS_CHOICES = (
        ('Draft', 'draft'),
        ('Published', 'published'))

    status = m.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    def get_absolute_url(self):
        return reverse('blog:about_post', kwargs = {'pk': self.pk})
        
    #-------------- Managers --------------------------
    objects = m.Manager()
    published = PublishedManager()
    """
        published - Query set manager where all objects is 'posts with published status. 
        at: class PublishedManager'

    """

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name, verbose_name_plural = "Post", "Postlar"


# this comment model uses in blog, vacancy.. to_item -> post for blog, vacancy for vacancy app
class Comment(m.Model):
    author = m.ForeignKey(User,verbose_name='müəllif', related_name = 'comments', null = True, on_delete=m.SET_NULL)
    post = m.ForeignKey(Post, related_name = 'comments', on_delete = m.CASCADE)
    vacancy = m.ForeignKey('vacancy.Vacancy', related_name='comments', on_delete=m.CASCADE)
    email = m.EmailField('Elektron poçt')
    body = m.TextField('Şərh')
    created = m.DateTimeField('Yaradılma tarixi',auto_now_add = True)
    updated = m.DateTimeField('Yenilənmə tariix', auto_now = True)
    active = m.BooleanField('Aktiv', default = True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
         return f'Comment to -- " by {self.author} on: {self.created}'
