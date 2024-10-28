from django.db import models
from accounts.models import User, ParalympicSwimmerProfile


class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    participants = models.ManyToManyField(
        ParalympicSwimmerProfile, related_name="events_participating", blank=True
    )


class Result(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="results")
    athlete = models.ForeignKey(ParalympicSwimmerProfile, on_delete=models.CASCADE)
    position = models.PositiveIntegerField()
    time = models.DurationField(null=True, blank=True)
    notes = models.TextField(blank=True)
