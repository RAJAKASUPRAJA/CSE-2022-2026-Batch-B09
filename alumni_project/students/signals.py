from datetime import date
from django.db.models.signals import post_save
from django.dispatch import receiver

from accounts.models import User
from students.models import StudentProfile
from alumni.models import AlumniProfile


@receiver(post_save, sender=StudentProfile)
def convert_student_to_alumni(sender, instance, **kwargs):
    current_year = date.today().year

    if current_year > instance.graduation_year:
        user = instance.user

        # Convert role if not already alumni
        if user.role == "STUDENT":
            user.role = "ALUMNI"
            user.save()

            # Create AlumniProfile if not exists
            AlumniProfile.objects.get_or_create(
                user=user,
                defaults={
                    "company": "",
                    "job_role": "",
                    "experience": 0,
                    "industry": "",
                    "skills": "",
                }
            )
