# from celery_test.celery import app
#
#
# @app.task
# def add(x, y):
#     return x + y
from celery import shared_task

@shared_task(bind=True)
def fun(self):
    # operations
    print("You are in Fun function")
    return "done"