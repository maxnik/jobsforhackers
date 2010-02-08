# this file is modified version of the one from http://github.com/davepeck/CityGoRound.git
import os

RUNNING_APP_ENGINE_LOCAL_SERVER = os.environ.get('SERVER_SOFTWARE', 'Dev').startswith('Dev')

DEBUG = RUNNING_APP_ENGINE_LOCAL_SERVER # For now

APPEND_SLASH = False

INSTALLED_APPS = ['jobs']

MIDDLEWARE_CLASSES = [
    'django.middleware.common.CommonMiddleware',
    'django.middleware.http.ConditionalGetMiddleware',
]

DEBUG_SESSIONS = False # Set to True to get log lines about the contents of the session object

# NOTE davepeck:
#
# Add the following middleware classes
# if you want support for users in this application
# (I wrote these classes myself for another project)
#
# 'citygoround.middleware.AppEngineGenericUserMiddleware',


ROOT_URLCONF = 'urls'

# TEMPLATE_CONTEXT_PROCESSORS = ['citygoround.context.api_keys'] 

# NOTE davepeck:
#
# (also add the following context processor if you want user support)
#
# 'citygoround.context.appengine_user'

TEMPLATE_DEBUG = DEBUG

TEMPLATE_DIRS = [os.path.join(os.path.dirname(__file__), 'templates')]

TEMPLATE_LOADERS = ['django.template.loaders.filesystem.load_template_source']

FILE_UPLOAD_HANDLERS = ['django.core.files.uploadhandler.MemoryFileUploadHandler']

FILE_UPLOAD_MAX_MEMORY_SIZE = 10485760 # 10 MB -- an appengine maximum
MAX_IMAGE_SIZE = 983040  # 960 KB per image -- slightly under 1MB to guard against issues with db.put()

SERIALIZATION_SECRET_KEY = '\xcfB\xf6\xfa\x07\x8atE\xdc\xec\xf9zaR\xa4\x13\x88\xb9\xc4\xe4'

MEMCACHE_DEFAULT_SECONDS = 60 * 60
MEMCACHE_PAGE_SECONDS = MEMCACHE_DEFAULT_SECONDS
MEMCACHE_API_SECONDS = 24 * 60 * 60
MEMCACHE_SCREENSHOT_SECONDS = MEMCACHE_DEFAULT_SECONDS
MEMCACHE_SCREENSHOT_MAX_SIZE = 65536 # empirically, 64kb is a good max size for caching screen shots. This covers all the gallery page and home page screen shots.

REDIRECT_FIELD_NAME = "redirect_url"

if DEBUG:
    PROGRESS_DEBUG_MAGIC = "DEBUG"
else:
    PROGRESS_DEBUG_MAGIC = None

# only use local_settings.py if we're running debug server
if RUNNING_APP_ENGINE_LOCAL_SERVER:
    try:
        from local_settings import *
    except ImportError, exp:
        pass
