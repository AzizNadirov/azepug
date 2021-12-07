from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey
from blog.models import Tag
from vacancy.models import Employer



class Event(models.Model):
    author = ForeignKey(User, related_name = "created_events", on_delete = models.CASCADE)
    organiser = ForeignKey(Employer, related_name = "events", on_delete = models.CASCADE, verbose_name="Təşkilatçı")
    title = models.CharField("Tədbir", max_length=128)
    date_created = models.DateTimeField("Yaradılma tarixi", auto_now_add=True)
    starts_at = models.DateTimeField("Başlanma tarixi")
    ends_at = models.DateTimeField("Sonlanma tarixi")
    desc = models.TextField("Təsviri")
    tags = models.ManyToManyField(Tag, related_name="events")

    def get_absolute_url(self):
        return reverse('about_event', kwargs = {'pk': self.pk})

    def __str__(self):
        return f"[{self.title}]{self.author.username}"

class Comment(models.Model):
    author = models.ForeignKey(User,verbose_name='müəllif', related_name = 'e_comments', 
        null = True, on_delete=models.SET_NULL)
    event = models.ForeignKey(Event, related_name = 'comments', on_delete = models.CASCADE)
    body = models.TextField('Şərh', max_length = 1024)
    created = models.DateTimeField('Yaradılma tarixi',auto_now_add = True)
    updated = models.DateTimeField('Yenilənmə tariix', auto_now = True)
    active = models.BooleanField('Aktiv', default = True)
    image = models.ImageField(null = True, blank = True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
         return f'Comment to -- " by {self.author} on: {self.created}'