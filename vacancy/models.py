from django.db import models
from django.conf import settings

from django.urls import reverse
from taggit.managers import TaggableManager
from base.models import  AbstractComment, AbstractPost



class Employer(models.Model):
    name = models.CharField( "Name" ,max_length=128)
    workers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name = "works_at", verbose_name = "workers", blank = True)
    founded_at = models.DateField("Date created", null = True, blank = True)


    def __str__(self):
        return f"{self.name}"


class Vacancy(AbstractPost):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    employer = models.ForeignKey(Employer, related_name = 'vacancies', on_delete=models.CASCADE)
    dead_line = models.DateField("Date expiration (YYYY-MM-DD)", null=True)
    freelance = models.BooleanField("Remote")
    contact = models.CharField( "Contact" ,max_length=128)
    min_salary = models.PositiveIntegerField("Min salary")
    tags = TaggableManager()
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="liked_vacancy", blank = True, null = True)
    like_count = models.IntegerField(default=0)


    def get_absolute_url(self):
        return reverse('vacancy_detail', kwargs = {'pk': self.pk})

    class Meta:
        verbose_name = 'vacancy'
        verbose_name_plural = 'vacancies'
    def __str__(self):
        return f'{self.title} - {self.author}'


class Comment(AbstractComment):
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name='müəllif', related_name = 'v_comments', on_delete=models.CASCADE)

    def __str__(self):
        return f'Comment {self.author} to {self.vacancy}'
