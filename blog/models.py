from django.db import models
from django.conf import settings
from django.utils import timezone

class Post(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    title = models.CharField(
        verbose_name='Title',
        max_length=200
    )
    content = models.TextField(
        verbose_name='Content'
    )
    category = models.CharField(
        verbose_name='Category',
        max_length=15,
        default='Software'
    )
    published_date = models.DateTimeField(
        blank=True
    )

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    content = models.TextField()
    published_date = models.DateTimeField()


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.content
