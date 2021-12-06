from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import os

from django.urls.base import reverse
from azepug.settings import MEDIA_ROOT
from events.models import Event


def photo_upload(instance, filename):
    dir = os.path.join(MEDIA_ROOT,'profile_images',f'{instance.user.username}' )
    walk = list(os.walk(dir))
    try:
        for old_photo in walk[-1][-1]:
            os.remove(os.path.join(dir,old_photo))
    except: IndexError
    return f'profile_images/{instance.user.username}/{filename}'


class Contacts(models.Model):
    email = models.EmailField()
    github = models.URLField()
    linkedin = models.URLField()
    phone = models.CharField(max_length=10)



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField("Profil şəkli", upload_to=photo_upload, default = 'default_avatar.jpg', null=True)
    bio = models.TextField(max_length=1024)
    contacts = models.ManyToManyField(Contacts, related_name='profiles')
    events = models.ManyToManyField(Event, related_name="participants", null = True)

    
    
    def get_absolute_url(self):
        return reverse('user', kwargs = {'pk': self.pk})
    
    def __str__(self):
        return f'{self.user.username} Profile' 


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.image:
            self.image = f"{os.path.join(MEDIA_ROOT, 'profile_pics')}/default_avatar.jpg"
        else:
            img = Image.open(self.image.path)
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.image.path)
