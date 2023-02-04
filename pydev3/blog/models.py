from django.db import models
from django.core.validators import MaxValueValidator

class Post(models.Model):
    title = models.CharField('ブログタイトル', unique=True, max_length=10, null=False)
    content = models.TextField('本文', max_length=5000, null=False)
    image = models.ImageField('画像', null=True, blank=True, upload_to='blog_images/')

    def __str__(self):
        return self.title
