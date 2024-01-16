from django.db import models
from django.contrib.auth.models import User


class Entry(models.Model):
    """Something that the user felt inspired to write today"""

    text = models.TextField()
    date_added = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "entries"

    def __str__(self):
        """Return string representation of the model"""
        return self.text[:20] + "..."
