from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey
from blog.models import Tag
from vacancy.models import Employer
from base.models import AbstractComment



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

class Comment(AbstractComment):
    author = models.ForeignKey(User,verbose_name='müəllif', related_name = 'e_comments', 
        null = True, on_delete=models.SET_NULL)
    event = models.ForeignKey(Event, related_name = 'e_comments', on_delete = models.CASCADE)

    def __str__(self):
         return f'Comment to -- " by {self.author} on: {self.created}'