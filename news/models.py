from django.db import models
from django.contrib.auth.models import User


class News(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='news_images/', blank=True, null=True)
    file = models.FileField(upload_to='news_files/', blank=True, null=True)

    def __str__(self):
        return self.title


