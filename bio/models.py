from django.db import models

class Bio(models.Model):
    name = models.CharField(max_length=120)
    job_title = models.CharField(max_length=160)
    profile_picture = models.ImageField(upload_to='profile/', blank=True, null=True)
    description = models.TextField()

    # Optional contact info (kept simple)
    phone = models.CharField(max_length=40, blank=True)
    email = models.EmailField(blank=True)
    linkedin_url = models.URLField(blank=True)

    def __str__(self):
        return self.name
