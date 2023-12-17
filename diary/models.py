from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Diary(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    diary = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Diaries"

    def __str__(self):
        return self.title
