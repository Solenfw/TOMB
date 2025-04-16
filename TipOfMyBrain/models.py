
from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class UserAnswer(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    correct_answer = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        self.correct_answer = self.correct_answer.lower()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.correct_answer
