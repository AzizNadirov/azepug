from django.db import models as m
from django.contrib.auth.models import User
from django.urls import reverse


class Vacancy(m.Model):
    author = m.ForeignKey(User, on_delete=m.CASCADE)
    title = m.CharField('Bashliq', max_length = 50)
    content = m.TextField('Vakansiya')
    dead_line = m.DateField("Bitmə tarixi (YYYY-MM-DD)", null=True)
    date_created = m.DateField("Yaradılma tarixi", auto_now_add=True)
    freelance = m.BooleanField("Freelance imkanı")


    def get_absolute_url(self):
        return reverse('vacancy:about_vacancy', kwargs = {'pk': self.pk})

    class Meta:
        verbose_name = 'Vakansiya'
        verbose_name_plural = 'Vakansiyalar'
    def __str__(self):
        return f'{self.title} - {self.author}'
