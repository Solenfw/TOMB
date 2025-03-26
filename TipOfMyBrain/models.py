from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class UserAnswer(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user_guess = models.CharField(max_length=255)
    is_correct = models.BooleanField()

    def __str__(self):
        return f"{self.user_guess} : {'Correct<3' if self.is_correct else 'Wrong!'}"


