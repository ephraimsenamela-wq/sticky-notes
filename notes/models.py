from django.db import models


class Note(models.Model):
    """Sticky note model: title + content (+ colour & timestamps)."""

    COLOR_CHOICES = [
        ("yellow", "Yellow"),
        ("pink", "Pink"),
        ("green", "Green"),
        ("blue", "Blue"),
        ("purple", "Purple"),
    ]

    title = models.CharField(max_length=200)
    content = models.TextField()
    color = models.CharField(max_length=10, choices=COLOR_CHOICES, default="yellow")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-updated_at"]

    def __str__(self):
        return self.title
