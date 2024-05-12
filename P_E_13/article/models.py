from django.db import models
from django.urls import reverse


class Article(models.Model):
    image = models.ImageField(upload_to='images/blog')
    image_full = models.ImageField(upload_to='images/blog/full')
    category = models.CharField(max_length=20, blank=True, null=True)
    title = models.CharField(max_length=50)
    body = models.TextField()
    creat_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ('-creat_at',)

    def __str__(self):
        return f'{self.title} - {self.creat_at}'

    def get_absolute_url(self):
        return reverse('article:detail_article', args=(self.id, self.slug))
