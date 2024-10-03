

from django.db import models
import datetime


from django.utils import timezone

from django.contrib import admin


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    time_pub = models.DateTimeField()
    @admin.display(
        boolean=True,
        ordering="time_pub",
        description="Published recently?",
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.time_pub <= now

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    vote = models.IntegerField(default=0)

