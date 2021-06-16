from django.db import models

# Create your models here.
class Inverter(models.Model):
    v_dc = models.FloatField()
    i_dc = models.FloatField()

class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()

