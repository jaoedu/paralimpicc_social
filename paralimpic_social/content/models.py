from django.db import models
from accounts.models import User, ParalympicSwimmerProfile, SponsorProfile

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=100)

class Webinar(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField()
    link = models.URLField()
    participants = models.ManyToManyField(ParalympicSwimmerProfile, related_name='webinars_attending', blank=True)