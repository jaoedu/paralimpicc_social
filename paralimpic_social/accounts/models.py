from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group


class User(AbstractUser):
    is_paralympic_swimmer = models.BooleanField(default=False)
    is_sponsor = models.BooleanField(default=False)
    profile_picture = models.ImageField(upload_to="profile_pics/", blank=True)
    groups = models.ManyToManyField(
        Group,
        related_name="accounts_user_set",
        blank=True,
        verbose_name="groups",
        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="accounts_user_permissions",
        blank=True,
        verbose_name="user permissions",
        help_text="Specific permissions for this user.",
    )


class ParalympicSwimmerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    functional_class = models.CharField(max_length=50)
    events = models.CharField(max_length=200)
    achievements = models.TextField(blank=True)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.group:
            swimmers_group = Group.objects.get_or_create(name="ParalympicSwimmers")[0]
            self.group = swimmers_group
            self.save()


class SponsorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=200)
    website = models.URLField(blank=True)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.group:
            sponsors_group = Group.objects.get_or_create(name="Sponsors")[0]
            self.group = sponsors_group
            self.save()
