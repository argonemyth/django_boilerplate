from .base import *

DEBUG = False 
TEMPLATE_DEBUG = False 
COMPRESS_ENABLED = True 

ADMINS = ( 
    ('Fei Tan', 'fei@argonemyth.com'),
)

ALLOWED_HOSTS = ['127.0.0.1', ]

# DB
DATABASES = { 
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', 
        'NAME': 'boilerplate',
        'USER': 'deploy',
        'PASSWORD': '', 
        'HOST': '',                      
        'PORT': '',                      
    }   
}

# Apps
INSTALLED_APPS+= (
    'djcelery',
    'kombu.transport.django',
    'gunicorn',    
)

# Cache
CACHES = { 
    'default': {
        'BACKEND': 'redis_cache.cache.RedisCache',
        'LOCATION': '127.0.0.1:6379',
        'KEY_PREFIX': 'boilerplate',
        'OPTIONS': {
            'CLIENT_CLASS': 'redis_cache.client.DefaultClient',
        }   
    }   
}

# Use the cached template loader
TEMPLATE_LOADERS = ( 
    ('django.template.loaders.cached.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )), 
)

# CELERY SETTINGS
# import djcelery
# djcelery.setup_loader()

# BROKER_URL = 'redis://'
# CELERY_SEND_TASK_ERROR_EMAILS = True
# CELERYD_LOG_COLOR = False


try:
    from .local import *
except ImportError:
    pass              
