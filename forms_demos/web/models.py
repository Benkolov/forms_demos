from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    hobby = models.CharField(max_length=50)
    is_happy = models.BooleanField(default=False)

    def __str__(self):
        return self.name

