from django.db import models

# Create your models here.
class poet_author(models.Model):
    author = models.CharField(max_length=60)

    def __str__(self):
        return self.author

class poets_shown(models.Model):
    poetAuthor = models.ForeignKey(poet_author,on_delete=models.CASCADE)
    poetName = models.CharField(max_length=60)
    poetContext = models.TextField(max_length=4000)
    popularity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.poetName