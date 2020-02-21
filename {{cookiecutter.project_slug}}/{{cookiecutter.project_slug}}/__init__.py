from .app_celery import {{ cookiecutter.project_slug }}_task as celery_app


__version__ = '{{ cookiecutter.version }}'
__all__ = [ 'celery_app', ]
