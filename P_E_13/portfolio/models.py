from django.db import models


class Portfolio(models.Model):
    name = models.CharField(max_length=20)
    title = models.CharField(max_length=40)
    image = models.ImageField(upload_to='staticfiles/images/portfolio')
    image_full = models.ImageField(upload_to='staticfiles/images/portfolio/full')
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.title}'
