from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name


class Movies(models.Model):
    title = models.CharField(max_length=250)
    overview = models.TextField()
    year = models.DateField()
    poster = models.ImageField(upload_to='movies/posters')
    video = models.FileField(upload_to='movies/videos')
    category = models.ManyToManyField(Category)
    def __str__(self):
        return self.title