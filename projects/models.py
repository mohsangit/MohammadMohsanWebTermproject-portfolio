from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    url = models.URLField(blank=True)

    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "name"]

    def __str__(self):
        return self.name
