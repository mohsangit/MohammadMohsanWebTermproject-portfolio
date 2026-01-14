from django.db import models

class Education(models.Model):
    title = models.CharField(max_length=200)
    institute = models.CharField(max_length=200)
    duration = models.CharField(max_length=100, blank=True)

    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "-id"]

    def __str__(self):
        return self.title
