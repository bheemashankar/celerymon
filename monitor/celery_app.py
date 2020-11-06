from __future__ import absolute_import
import os
from celery import Celery

app = Celery('celery_monitor',
             include=['monitor.tasks'])

app.config_from_object('monitor.config')

app.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'monitor.tasks.debug_task',
        'schedule': 30.0
    },
}