from django.db import models

class Experience(models.Model):
    title = models.CharField(max_length=200)          # e.g., "Data Scientist Intern"
    company = models.CharField(max_length=200, blank=True)
    role = models.CharField(max_length=200, blank=True)
    status = models.CharField(max_length=120, blank=True)  # e.g., "Ended", "Ongoing"
    details = models.TextField(blank=True)

    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "-id"]

    def __str__(self):
        return self.title
