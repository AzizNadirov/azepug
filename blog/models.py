from django.db import models as m
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


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
        return reverse('about_post', kwargs = {'pk': self.pk})
        
    #-------------- Managers --------------------------
    objects = m.Manager()
    published = PublishedManager()


    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name, verbose_name_plural = "Post", "Postlar"


class Comment(m.Model):
    author = m.ForeignKey(User,verbose_name='müəllif', related_name = 'b_comments', null = True, on_delete=m.SET_NULL)
    post = m.ForeignKey(Post, related_name = 'b_comments', on_delete = m.CASCADE)
    email = m.EmailField('Elektron poçt')
    body = m.TextField('Şərh')
    created = m.DateTimeField('Yaradılma tarixi',auto_now_add = True)
    updated = m.DateTimeField('Yenilənmə tariix', auto_now = True)
    active = m.BooleanField('Aktiv', default = True)
    image = m.ImageField(null = True, blank = True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
         return f'Comment to -- " by {self.author} on: {self.created}'

