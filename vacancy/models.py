from django.db import models as m
from django.contrib.auth.models import User
from django.urls import reverse
from blog.models import Tag
from base.models import  AbstractComment




class Employer(m.Model):
    name = m.CharField( "Adı" ,max_length=128)
    workers = m.ManyToManyField(User, related_name = "works_at", verbose_name = "Əməkdaşlar", null = True, blank = True)
    founded_at = m.DateField("Yaradılma tarixi", null = True)


    def __str__(self):
        return f"{self.name}"


class Vacancy(m.Model):
    author = m.ForeignKey(User, on_delete=m.CASCADE)
    employer = m.ForeignKey(Employer, related_name = 'vacancies', on_delete=m.CASCADE)
    title = m.CharField('Başlıq', max_length = 128)
    content = m.TextField('Məzmun')
    dead_line = m.DateField("Bitmə tarixi (YYYY-MM-DD)", null=True)
    date_created = m.DateField("Yaradılma tarixi", auto_now_add=True)
    freelance = m.BooleanField("Freelance imkanı")
    contact = m.CharField( "Əlaqə ünvanı" ,max_length=128)
    min_salary = m.PositiveIntegerField("Minimal maaş")
    tags = m.ManyToManyField(Tag, related_name="vacancies")


    def get_absolute_url(self):
        return reverse('about_vacancy', kwargs = {'pk': self.pk})

    class Meta:
        verbose_name = 'Vakansiya'
        verbose_name_plural = 'Vakansiyalar'
    def __str__(self):
        return f'{self.title} - {self.author}'


class Comment(AbstractComment):
    vacancy = m.ForeignKey(Vacancy, on_delete=m.CASCADE, related_name='v_comments')
    author = m.ForeignKey(User,verbose_name='müəllif', related_name = 'v_comments', on_delete=m.CASCADE)

    def __str__(self):
        return f'Comment to {self.vacancy} " by {self.author} on: {self.created_at}'
