from django.db import models
from accounts.models import User, ParalympicSwimmerProfile, SponsorProfile


class SponsorshipRequest(models.Model):
    sponsor = models.ForeignKey(
        SponsorProfile, on_delete=models.CASCADE, related_name="sponsorship_requests"
    )
    athlete = models.ForeignKey(
        ParalympicSwimmerProfile,
        on_delete=models.CASCADE,
        related_name="sponsorship_requests",
    )
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ("pending", "Pendente"),
            ("accepted", "Aceito"),
            ("rejected", "Rejeitado"),
        ],
        default="pending",
    )


class Follow(models.Model):
    follower = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="following"
    )
    followed = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="followers"
    )
    created_at = models.DateTimeField(auto_now_add=True)
