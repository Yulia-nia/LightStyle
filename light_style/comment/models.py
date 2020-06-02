from django.db import models
from django.utils import timezone
from users.models import User


class Comment(models.Model):
    title = models.CharField(max_length=80)
    author = models.ForeignKey(User, related_name='author', on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)
        verbose_name_plural = 'Все комментарии'
        verbose_name = 'Комментарий'

    def __str__(self):
        return 'Comment {} by {}'.format(self.title, self.author)