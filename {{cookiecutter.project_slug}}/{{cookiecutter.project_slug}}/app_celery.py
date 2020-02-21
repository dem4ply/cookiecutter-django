from __future__ import absolute_import

import os

from celery import Celery
from django.conf import settings


__all__ = [ '{{ cookiecutter.project_slug }}_task' ]

os.environ.setdefault( 'DJANGO_SETTINGS_MODULE', '{{ cookiecutter.project_slug }}.settings' )

{{ cookiecutter.project_slug }}_task = Celery( '{{ cookiecutter.project_slug }}' )

{{ cookiecutter.project_slug }}_task.config_from_object( 'django.conf:settings' )
{{ cookiecutter.project_slug }}_task.autodiscover_tasks( lambda: settings.INSTALLED_APPS )
