from django.db import models as m
class AbstractComment(m.Model):
    body = m.TextField('Şərh')
    created_at = m.DateTimeField('Yaradılma tarixi',auto_now_add = True)
    updated = m.DateTimeField('Yenilənmə tariix', auto_now = True)
    active = m.BooleanField('Aktiv', default = True)
    image = m.ImageField(null = True, blank = True)

    class Meta:
        abstract = True
        ordering = ('-created_at',)

    def __str__(self):
         return f'Comment to -- " by {self.author} on: {self.created_at}'