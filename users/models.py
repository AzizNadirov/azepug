from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from PIL import Image
import os

from django.urls.base import reverse
from azepug.settings import MEDIA_ROOT
from events.models import Event


def photo_upload(instance, filename):
    dir = os.path.join(MEDIA_ROOT,'profile_images',f'{instance.user_name}' )
    walk = list(os.walk(dir))
    try:
        for old_photo in walk[-1][-1]:
            os.remove(os.path.join(dir,old_photo))
    except: IndexError
    return f'profile_images/{instance.user_name}/{filename}'


class Contacts(models.Model):
    email = models.EmailField()
    github = models.URLField()
    linkedin = models.URLField()
    phone = models.CharField(max_length=10)



class ProfileManager(BaseUserManager):

    def create_superuser(self, email, user_name, first_name, password, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_active', True)
        return self.create_user(email, user_name, first_name, password, **kwargs)

    def create_user(self, email, user_name, first_name, password, **kwargs):
        email = self.normalize_email(email)
        user = self.model(email = email, user_name=user_name, first_name = first_name, **kwargs)
        user.set_password(password)
        ## do some validations
        user.save()
        return user


class Profile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    user_name = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    start_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to=photo_upload, default = 'default_avatar.jpg', null=True, blank = True)
    about = models.TextField(max_length=1024, blank = True, null = True)
    contacts = models.ManyToManyField(Contacts, related_name='profiles')
    events = models.ManyToManyField(Event, related_name="participants", null = True)
    is_staff = models.BooleanField(default = False)
    is_active = models.BooleanField(default = False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name']

    objects = ProfileManager()
    
    def get_absolute_url(self):
        return reverse('user', kwargs = {'pk': self.pk})
    
    def __str__(self):
        return f'{self.user_name}' 


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
