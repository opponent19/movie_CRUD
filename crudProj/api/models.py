from django.db import models
class Movie(models.Model):
    name = models.CharField(max_length=50)
    img = models.URLField(max_length=50)
    summary = models.TextField()
    
    def __str__(self):
        return self.name
    
