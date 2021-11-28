from django.db import models


# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    time_pup = models.DateTimeField()


class Choice(models.Model):
    # Neu quetion bi xoa di thi Answer cung bi delete
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)
    vote = models.IntegerField(default=0)
