from django.db import models

# Create your models here.
class poetsShown(models.Model):
    poetAuthor = models.CharField(max_length=60)
    poetName = models.CharField(max_length=60)
    poetContext = models.TextField(max_length=4000)

    def __str__(self):
        return self.poetName