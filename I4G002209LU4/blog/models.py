from django.db import models

# Create your models here.
class Members(models.Model):
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    author=models.ForeignKey(to='self', on_delete=models.CASCADE)
    created_date=models.DateTimeField()
    published_date=models.DateTimeField()