import os

DEBUG = False

APPEND_SLASH = False

INSTALLED_APPS = ['jobs']

MIDDLEWARE_CLASSES = [
    'django.middleware.common.CommonMiddleware',
    'django.middleware.http.ConditionalGetMiddleware',
]

ROOT_URLCONF = 'urls'

TEMPLATE_DEBUG = False

TEMPLATE_DIRS = [os.path.join(os.path.dirname(__file__), 'templates')]

TEMPLATE_LOADERS = ['django.template.loaders.filesystem.load_template_source']

FILE_UPLOAD_HANDLERS = ['django.core.files.uploadhandler.MemoryFileUploadHandler']

FILE_UPLOAD_MAX_MEMORY_SIZE = 10485760 # 10 MB -- an appengine maximum
MAX_IMAGE_SIZE = 983040  # 960 KB per image -- slightly under 1MB to guard against issues with db.put()

SERIALIZATION_SECRET_KEY = '\xcfB\xfa\x07\x8atE\xdc\xec\xf9zaR\xa4\x13\x88\xf6\xb9\xc4\xe4'

MEMCACHE_DEFAULT_SECONDS = 60 * 60
MEMCACHE_PAGE_SECONDS = MEMCACHE_DEFAULT_SECONDS
MEMCACHE_API_SECONDS = 24 * 60 * 60
MEMCACHE_SCREENSHOT_SECONDS = MEMCACHE_DEFAULT_SECONDS
MEMCACHE_SCREENSHOT_MAX_SIZE = 65536 # empirically, 64kb is a good max size for caching screen shots. This covers all the gallery page and home page screen shots.

REDIRECT_FIELD_NAME = "redirect_url"

