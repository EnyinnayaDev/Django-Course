"""User models for the application."""

from django.db import models


class Students(models.Model):
    """Model representing a student."""
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    level = models.IntegerField()
    
    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"

    def __str__(self):
        return self.name
