from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from distutils.command.upload import upload


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField('Profile picture', upload_to='profiles', null=True, blank=True)
    description = models.TextField('Description', max_length=255, blank=True, null=True)
    created = models.DateTimeField('Created', default=timezone.now())

    class Meta:
        verbose_name = 'Profile'

    def __str__(self):
        return self.user.username

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField('Name', max_length=50)
    picture = models.ImageField('Post picture', upload_to='posts', height_field=320, width_field=320, null=True, blank=True)
    content = models.TextField('Content', blank=False, null=False)
    created = models.DateTimeField('Created', editable=False, default=timezone.now())

    class Meta:
        verbose_name = 'Post'

    def __str__(self):
        return self.name

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField('Content', blank=False, null=False)
    created = models.DateTimeField('Created', editable=False, default=timezone.now())
    edited = models.DateTimeField('Edited', default=timezone.now())

    class Meta:
        verbose_name = 'Comment'

    def __str__(self):
        return f'Comentario de {self.user.username}'
