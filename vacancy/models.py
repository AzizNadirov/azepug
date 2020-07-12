from django.db import models as m

class Ability(m.Model):
    ability = m.CharField('Bacarıq', max_length=25, null=False, default='Python')

    class Meta:
        verbose_name = 'Bacarıq'
        verbose_name_plural = 'Bacarıqlar'
class Requirments(m.Model):
    high_edu = m.BooleanField('Ali təhsil', default=True)
    experience = m.PositiveSmallIntegerField('Minimum iş təcrübəsi', null=True)

class Vacancy(m.Model):
    title = m.TextField(max_length=50)
    abilities = m.ManyToManyRel(Ability)
    requirments = m.ManyToManyRel(Requirments)
    STATUS_CHOİCES = (
        ('AZN, manat'),
        ('USD', 'ABŞ_dolları'),
        ('RB', 'Rusiya_rublu'),
        ('Başqa', 'başqa')
    )
    celery = m.FloatField("Maaş")
    currancy_of_celery = m.CharField('Valyuta', choices=STATUS_CHOİCES, max_length=20)
    date_published = m.DateField(auto_now=True)
    dead_line = m.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Vakansiya'
        verbose_name_plural = 'Vakansiyalar'
    
    def __str__(self):
        return f'{self.title}\t{self.dead_line}'