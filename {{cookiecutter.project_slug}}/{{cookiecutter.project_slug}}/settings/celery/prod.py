import os

# from kombu import Exchange, Queue
# from celery.schedules import crontab
# from datetime import timedelta


user = os.environ[ '{{ cookiecutter.project_slug|upper }}__RABBITMQ__USER' ]
password = os.environ[ '{{ cookiecutter.project_slug|upper }}__RABBITMQ__PASSWORD' ]
vhost = os.environ[ '{{ cookiecutter.project_slug|upper }}__RABBITMQ__VHOST' ]
port = os.environ[ '{{ cookiecutter.project_slug|upper }}__RABBITMQ__PORT' ]
domain = os.environ[ '{{ cookiecutter.project_slug|upper }}__RABBITMQ__DOMAIN' ]
celery_url = f"amqp://{user}:{password}@{domain}:{port}/{vhost}"

CELERY_BROKER_URL = celery_url
CELERY_RESULT_BACKEND = 'rpc://'

CELERY_TASK_ANNOTATIONS = { }

CELERY_TASK_QUEUES = (
    Queue(
        '{{ cookiecutter.project_slug|lower }}.default',
        Exchange( 'task', 'topic' ),
        routing_key='default' ),
    Queue(
        'debug', Exchange( 'task_debug', 'topic' ), routing_key='*.debug.*' ),
)

CELERY_TASK_DEFAULT_QUEUE = '{{ cookiecutter.project_slug|lower }}.default'
CELERY_TASK_DEFAULT_EXCHANGE = "tasks"
CELERY_TASK_DEFAULT_EXCHANGE_TYPE = "topic"
CELERY_TASK_DEFAULT_ROUTING_KEY = "task.default"

CELERY_TASK_ROUTES = {
    '{{ cookiecutter.project_slug|lower }}.default': {
        'binding_key': 'task.#',
    },
    '{{ cookiecutter.project_slug|lower }}.tasks.debug_task': {
        'queue': 'debug',
        'binding_key': 'task.debug.*',
        'exchange': 'task_debug'
    },
}

CELERY_BEAT_SCHEDULE = { }

CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'

CELERY_ALWAYS_EAGER = False
CELERY_TASK_ALWAYS_EAGER = False
