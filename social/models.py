from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from distutils.command.upload import upload


# Create your models here.
class Profile(models.Model):    # extiende el modelos User
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    picture = models.ImageField('Profile picture', default='profiles/default.png', upload_to='profiles', blank=True)
    description = models.TextField('Description', max_length=255, blank=True)
    created = models.DateTimeField('Created', default=timezone.now())

    class Meta:
        verbose_name = 'Profile'

    def __str__(self):
        return self.user.username

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')  # con el related_name puedo acceder desde una instancia usuario a sus posts (es decir, el revés)
    name = models.CharField('Name', max_length=50)
    picture = models.ImageField('Post picture', upload_to='posts', blank=True)
    content = models.TextField('Content', blank=False, null=False)
    created = models.DateTimeField('Created', editable=False, default=timezone.now())

    class Meta:
        verbose_name = 'Post'

    def __str__(self):
        return self.name

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField('Content', blank=False, null=False)
    created = models.DateTimeField('Created', editable=False, default=timezone.now())
    edited = models.DateTimeField('Edited', default=timezone.now())

    class Meta:
        verbose_name = 'Comment'

    def __str__(self):
        return f'Comentario de {self.user.username}'


# El siguiente código puede crearse en otro fichero signals.py
# Fuente: https://realpython.com/django-social-network-1/#step-3-implement-a-post-save-hook 
from django.db.models import signals
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()

# Create a Profile for each new user.
signals.post_save.connect(create_profile, sender=User)  # Invocará la función create_profile() cada vez que se ejecute .save() del modelo User -parámetro "sender"- (de ahí viene el nombre post-save)