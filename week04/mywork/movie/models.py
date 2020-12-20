from django.db import models

# Create your models here.
class Comment(models.Model):
    movie = models.ForeignKey('Movie', models.DO_NOTHING, blank=True, null=True)
    star = models.CharField(max_length=64, blank=True, null=True)
    comm = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comment'

class Movie(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movie'