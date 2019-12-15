from django.db import models

# Create your models here.
class hello_world(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    technology=models.CharField(max_length=100)
    image=models.FilePathField(path="/img")