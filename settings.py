import os

DEBUG = True

APPEND_SLASH = False

INSTALLED_APPS = ['jobs']

MIDDLEWARE_CLASSES = [
    'google.appengine.ext.appstats.recording.AppStatsDjangoMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.http.ConditionalGetMiddleware',
]

ROOT_URLCONF = 'urls'

TEMPLATE_DEBUG = True

TEMPLATE_DIRS = [os.path.join(os.path.dirname(__file__), 'templates')]

TEMPLATE_LOADERS = ('django.template.loaders.filesystem.load_template_source',)

TEMPLATE_CONTEXT_PROCESSORS = ('jobs.views._auth_processor',)

SERIALIZATION_SECRET_KEY = '\xcfB\xfa\x07\x8atE\xdc\xec\xf9zaR\xa4\x13\x88\xf6\xb9\xc4\xe4'

REDIRECT_FIELD_NAME = "redirect_url"

USE_I18N = False
