from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.translation import gettext_lazy as _


class Portfolio(models.Model):
    name = models.CharField(max_length=20)
    title = models.CharField(max_length=40)
    description = RichTextUploadingField(verbose_name=_("description"), blank=True, null=True)
    image = models.ImageField(upload_to='images/portfolio')
    image_full = models.ImageField(upload_to='images/portfolio/full', blank=True, null=True)
    video = models.FileField(upload_to='videos/portfolio', blank=True, null=True)
    creat_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ('-creat_at',)

    def __str__(self):
        return f'{self.name} - {self.creat_at}'

    def get_absolute_url(self):
        return reverse('portfolio:detail_portfolio', args=(self.id, self.slug))
