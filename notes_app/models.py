from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")
    title = models.CharField(max_length=200)
    content = models.TextField()
    pinned = models.BooleanField(default=False)
    color = models.CharField(
        max_length=20,
        default="yellow",
        choices=[
            ("yellow", "Yellow"),
            ("blue", "Blue"),
            ("green", "Green"),
            ("red", "Red"),
            ("purple", "Purple"),
            ("white", "White"),
        ]
    )
    archived = models.BooleanField(default=False)
    trashed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    reminder_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title
