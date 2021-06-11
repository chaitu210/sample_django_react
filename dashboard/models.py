from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=120)
    url = models.TextField()
    abstract = models.TextField()
    body_text = models.TextField()
    body_html = models.TextField()
    genre = models.CharField(max_length=120)

    def __str__(self):
        return self.title