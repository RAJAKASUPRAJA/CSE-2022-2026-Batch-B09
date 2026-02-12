from django.db import models
from django.conf import settings


class StudentProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="student_profile"
    )
    department = models.CharField(max_length=100)
    skills = models.TextField(help_text="Comma separated skills")
    career_interest = models.CharField(max_length=200)
    graduation_year = models.IntegerField()
    resume = models.FileField(upload_to="resumes/", blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.email
from alumni.models import AlumniProfile


class Connection(models.Model):

    STATUS_CHOICES = (
        ("REQUESTED", "Requested"),
        ("ACCEPTED", "Accepted"),
        ("REJECTED", "Rejected"),
    )

    student = models.ForeignKey(
        StudentProfile,
        on_delete=models.CASCADE,
        related_name="connections"
    )
    alumni = models.ForeignKey(
        AlumniProfile,
        on_delete=models.CASCADE,
        related_name="connections"
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="REQUESTED"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.user.email} → {self.alumni.user.email}"
