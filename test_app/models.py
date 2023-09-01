from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    probation = models.DecimalField(
        max_digits=2,
        decimal_places=1
    )
    position = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name + ' ' + self.position


class Order(models.Model):
    task_id = models.UUIDField()
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=550)
    employee = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='orders'
    )

    def __str__(self):
        return self.name
