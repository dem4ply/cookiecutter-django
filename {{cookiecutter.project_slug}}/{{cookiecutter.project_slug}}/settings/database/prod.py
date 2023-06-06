import os


#mysql
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ[ '{{ cookiecutter.project_slug|upper }}__DATABASE__NAME' ],
        'USER': os.environ[ '{{ cookiecutter.project_slug|upper }}__DATABASE__USER' ],
        'PASSWORD': os.environ[ '{{ cookiecutter.project_slug|upper }}__DATABASE__PASSWORD' ],
        'HOST': os.environ[ '{{ cookiecutter.project_slug|upper }}__DATABASE__HOST' ],
        'PORT': os.environ[ '{{ cookiecutter.project_slug|upper }}__DATABASE__PORT' ],
    },
}
