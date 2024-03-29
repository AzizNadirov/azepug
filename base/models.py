from django.db import models as m
from django.utils import timezone
from ckeditor.fields import RichTextField





class AbstractPost(m.Model):
    title = m.CharField("Başlıq", max_length = 128)
    content = RichTextField()
    date_created = m.DateTimeField("Yaradılma tarixi", default= timezone.now)
    drafted = m.BooleanField(verbose_name="Qaralama", default = False)
    views = m.IntegerField(verbose_name="", default=0)

    class Meta:
        abstract = True
        ordering = ('-date_created',)



class AbstractComment(m.Model):
    body = m.TextField('Şərh')
    created_at = m.DateTimeField('Yaradılma tarixi',auto_now_add = True)
    updated = m.DateTimeField('Yenilənmə tariix', auto_now = True)
    active = m.BooleanField('Aktiv', default = True)

    class Meta:
        abstract = True
        ordering = ('-created_at',)

    def __str__(self):
         return f'Comment to -- " by {self.author} on: {self.created_at}'

