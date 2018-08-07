from django.db import models

# Create your models here.
class Question(models.Model):
    question = models.CharField(max_length=250, blank=True, null=True)
    correct_answer = models.CharField(max_length=250, blank=True, null=True)
    wrong_answer1 = models.CharField(max_length=250, blank=True, null=True)
    wrong_answer2 = models.CharField(max_length=250, blank=True, null=True)
    wrong_answer3 = models.CharField(max_length=250, blank=True, null=True)
    
    def __str__(self):
        return self.question