from django.db import models
from django.contrib.auth.models import AbstractUser
from random import randint

# Create your models here.


class User(AbstractUser):
    probation = models.DecimalField(
        max_digits=2,
        decimal_places=1
    )
    position = models.CharField(max_length=100)


class Order(models.Model):
    task_id = models.CharField(max_length=8)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=550)
    employee = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='orders'
    )

    def save(self, **kwargs):
        self.task_id = ''.join([str(randint(0, 8)) for number in range(0, 8)])
        super().save(**kwargs)
