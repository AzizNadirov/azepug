from django.db import models
from django.urls import reverse
from users.models import User
from blog.models import Tag


class Comment(models.Model):
    author = models.ForeignKey(User, verbose_name='müəllif', related_name = 'f_comments', 
        null = True, on_delete=models.SET_NULL)
    answer = models.ForeignKey('Answer', related_name = 'comments', on_delete = models.CASCADE)
    body = models.TextField('Şərh', max_length = 1024)
    created = models.DateTimeField('Yaradılma tarixi',auto_now_add = True)
    updated = models.DateTimeField('Yenilənmə tariix', auto_now = True)
    active = models.BooleanField('Aktiv', default = True)
    image = models.ImageField(null = True, blank = True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
         return f'{self.author} - comment to answer: {self.answer}'


class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="questions")
    title = models.CharField(verbose_name = "Başlıq",max_length=128)
    body = models.TextField(verbose_name= "Məzmun")
    supports = models.IntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    last_edited = models.DateTimeField(auto_now = True)
    tags = models.ManyToManyField(Tag, related_name= "questions")


    def __str__(self):
        return f"{self.title[:51]} : {self.author.username}"


    # def get_absolute_url(self):
    #     return reverse('question_detail', kwargs = {'pk': self.id})



class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="answers")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name= "answers")
    body = models.TextField(verbose_name= "Məzmun")
    supports = models.IntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add = True)
    last_edited = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f"Answer {self.author} to {self.question.title}"

    # def get_absolute_url(self):
    #     return reverse('answer_detail', kwargs = {'a_pk': self.pk})
