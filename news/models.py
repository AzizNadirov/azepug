from django.db import models
from django.contrib.auth.models import User
from django.urls.base import reverse
from blog.models import Tag 



class Comment(models.Model):
    author = models.ForeignKey(User,verbose_name='müəllif', related_name = 'n_comments', null = True, on_delete=models.SET_NULL)
    news = models.ForeignKey('News', related_name = 'n_comments', on_delete = models.CASCADE)
    email = models.EmailField('Elektron poçt')
    body = models.TextField('Şərh')
    created = models.DateTimeField('Yaradılma tarixi',auto_now_add = True)
    updated = models.DateTimeField('Yenilənmə tariix', auto_now = True)
    active = models.BooleanField('Aktiv', default = True)
    image = models.ImageField(null = True, blank = True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
         return f'Comment to -- " by {self.author} on: {self.created}'

class News(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "news")
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=128)
    body = models.TextField(max_length=2048)
    image = models.ImageField()
    tags = models.ManyToManyField(Tag, related_name = 'news')
    drafted = models.BooleanField(default=False)

    def __str__(self):
        return f"News: {self.title} : {self.author}"
    
    def get_absolute_url(self):
        return reverse("news_detail", kwargs={"pk": self.pk})
