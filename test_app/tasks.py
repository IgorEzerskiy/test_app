from __future__ import absolute_import, unicode_literals
from random import randint
from test_task.celery import app
from celery import current_task
from test_app.models import Order, User


@app.task()
def add_order():
    users = User.objects.all()
    random_position = randint(0, len(users)-1)
    Order.objects.create(
        task_id=current_task.request.id,
        name='Замовлення',
        description='опис',
        employee=users[random_position]
    )
