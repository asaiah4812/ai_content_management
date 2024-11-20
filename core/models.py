from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from django_resized import ResizedImageField
import os
from django.conf import settings
import uuid
from django_countries.fields import CountryField
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    addressLine1 = models.CharField(max_length=100, null=True, blank=True)
    addressLine2 = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    country = CountryField(blank_label='(Select country)', max_length=100, null=True, blank=True)
    postalCode = models.CharField(max_length=100, null=True, blank=True)
    profileImage = ResizedImageField(size=[200, 200], quality=90, upload_to='profile_images', null=True, blank=True)
    #   utility variable
    uniqueId = models.CharField(max_length=100, unique=True, default=uuid.uuid4, blank=True, null=True, editable=False)
    slug = models.SlugField(null=True, blank=True, max_length=500)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'Profile {self.user.username}'

    def get_absolute_url(self):
        return reverse('profile-detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if self.date_created is None:
             self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid()).split('-')[4]
        
        self.slug = slugify('{}'.format(self.user.username))
        self.last_updated = timezone.localtime(timezone.now())
        super(Profile, self).save(*args, **kwargs)

    @property
    def get_profile_image(self):
        if self.profileImage:
            return self.profileImage.url
        else:
            return settings.MEDIA_URL + 'image/icons/user.png'


class Task(models.Model):
    TASK_CATEGORY = (
        ('Work', 'Work'),
        ('Personal', 'Personal'),
        ('Other', 'Other')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=100, choices=TASK_CATEGORY)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']


    def __str__(self):
        return self.title


# class Follow(models.Model):
#     follower = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
#     following = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)