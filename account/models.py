from django.db import models


class Data(models.Model):
    name = models.CharField(max_length=20)
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text