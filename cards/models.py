from django.core.validators import MinLengthValidator
from django.db import models
from django.conf import settings


class Box(models.Model):
    name = models.CharField(max_length=50, validators=[MinLengthValidator(3)])
    capacity = models.IntegerField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    state = models.IntegerField(choices=((0, "Public"), (1, "Private")), default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name


class Card(models.Model):
    question = models.CharField(max_length=300,  validators=[MinLengthValidator(3)])
    answer = models.CharField(max_length=300, validators=[MinLengthValidator(3)])
    box = models.ForeignKey(Box, on_delete=models.CASCADE, null=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question
