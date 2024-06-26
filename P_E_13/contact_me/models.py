from django.db import models


class UserContact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-timestamp',)

    def __str__(self):
        return f'{self.name}-{self.timestamp}'

