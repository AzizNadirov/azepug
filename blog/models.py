from django.db import models as m
from django.contrib.auth.models import User as U
from django.utils import timezone
from django.urls import reverse


class PublishedManager(m.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset().filter(status = 'Published')
    

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
    author = m.ForeignKey(U, on_delete=m.CASCADE)
    date_created = m.DateTimeField(default= timezone.now)
    slug = m.SlugField(max_length=250, unique_for_date='date_created')
    STATUS_CHOICES = (
        ('Draft', 'draft'),
        ('Published', 'published'))

    status = m.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    # def get_absolute_url(self):
    #     return reverse('blog:about_post',
    #     args=[self.date_created.year, self.date_created.month, self.date_created.day, self.slug])
    #
    #-------------- Managers --------------------------
    objects = m.Manager()
    published = PublishedManager()

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name, verbose_name_plural = "Post", "Postlar"