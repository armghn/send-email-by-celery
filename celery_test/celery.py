# from celery import Celery
# from celery_test import settings
#
#
# app = Celery('celery_test')
#
# app.config_from_object('django.conf:settings', namespace='CELERY')
#
# app.conf.broker_url = 'redis://localhost:6379/0'
#
# app.autodiscover_tasks()

from __future__ import absolute_import,unicode_literals
import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "celery_test.settings")
app = Celery("celery_test")

#we are using asia/kolkata time so we are making it False
app.conf.enable_utc=False
app.conf.update(timezone='Asia/Kolkata')

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()

#CELERY BEAT SETTINGS
app.conf.beat_schedule = {

}

@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")