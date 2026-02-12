from django.db import models
from django.conf import settings


class AlumniProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="alumni_profile"
    )
    company = models.CharField(max_length=150)
    job_role = models.CharField(max_length=150)
    experience = models.IntegerField(help_text="Years of experience")
    industry = models.CharField(max_length=150)
    skills = models.TextField(help_text="Comma separated skills")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.email


class PlacementDetails(models.Model):

    STATUS_CHOICES = (
        ("PLACED", "Placed"),
        ("NOT_PLACED", "Not Placed"),
    )

    alumni = models.ForeignKey(
        AlumniProfile,
        on_delete=models.CASCADE,
        related_name="placements"
    )
    company = models.CharField(max_length=150)
    role = models.CharField(max_length=150)
    year = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.alumni.user.email} - {self.company}"
