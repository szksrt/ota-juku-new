from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField("タイトル", max_length=200)
    content = models.TextField("本文")
    published_date = models.DateTimeField("公開日", default=timezone.now)

    def __str__(self):
        return self.title