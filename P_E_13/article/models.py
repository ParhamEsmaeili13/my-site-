from django.db import models


class Article(models.Model):
    image = models.ImageField(upload_to='staticfiles/images/blog')
    category = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    body = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
