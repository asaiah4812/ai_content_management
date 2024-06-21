from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
import uuid
# Create your models here.

class Content(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('content:content-detail', args=[self.pk])

ALLOWED_EXTENSIONS = [
    '.pdf', '.docx', '.xlsx', '.pptx', '.jpg', '.jpeg', '.png', '.gif'
]


class Files(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    files = models.FileField(upload_to='content_files/', validators=[FileExtensionValidator(allowed_extensions=ALLOWED_EXTENSIONS)])
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content.title

    def delete(self, *args, **kwargs):
        for item in self.item_set.all():
            item.delete()
        super(Content, self).delete(*args, **kwargs)


