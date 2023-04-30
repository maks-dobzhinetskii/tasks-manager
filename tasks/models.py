from django.conf import settings
from django.db import models
from django.urls import reverse


class DraftManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(draft=True)


class Task(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(null=False)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)
    execute_at = models.DateTimeField(null=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    views = models.IntegerField(default=0, null=True, blank=True)
    draft = models.BooleanField(default=False)
    objects = models.Manager()
    draft_true = DraftManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("task_detail", args=[str(self.id)])
