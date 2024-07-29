from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
                                        
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
class Programador(models.Model):
    fullname = models.CharField(max_length=100) #crear variable char y la longitud
    nickname = models.CharField(max_length=50)
    age = models.PositiveSmallIntegerField() #crear variable int pequeña
    is_active = models.BooleanField(default=True) #crear variable boolean