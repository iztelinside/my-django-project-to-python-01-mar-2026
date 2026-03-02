from django.db import models

# Create your models here.

class Articles(models.Model):
    title = models.CharField("Model Title",max_length=100)
    anons = models.CharField("Model Anons",max_length=100)
    content = models.TextField("Model Content")
    date = models.DateTimeField("Model Date")
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"
