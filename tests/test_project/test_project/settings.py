import os

import django


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEBUG = True
SECRET_KEY = '*****'
INSTALLED_APPS = (
    'django.contrib.staticfiles',
    'compressor',
    'compressor_additional_compilers',
    'test_project.base',
    'test_project.app'
)
ROOT_URLCONF = 'test_project.urls'
STATIC_URL = '/static/'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder'
)

if django.VERSION < (1, 8):
    TEMPLATE_CONTEXT_PROCESSORS = [
        'django.template.context_processors.static'
    ]
else:
    TEMPLATES = [{
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.static'
            ]
        }
    }]

if django.VERSION < (1, 10):
    MIDDLEWARE_CLASSES = []
else:
    MIDDLEWARE = []

# django-compressor settings
COMPRESS_ROOT = os.path.join(BASE_DIR, 'compressor')
COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'compressor_additional_compilers.precompilers.SCSSCompiler'),
    ('module', 'compressor_additional_compilers.precompilers.ES6Compiler')
)
COMPRESS_ENABLED = False

# django-compressor-toolkit settings; see compressor_additional_compilers/apps.py for details
if 'COMPRESS_NODE_MODULES' in os.environ:
    COMPRESS_NODE_MODULES = os.getenv('COMPRESS_NODE_MODULES')
