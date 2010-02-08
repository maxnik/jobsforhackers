# NOTE: Must import *, since Django looks for things here, e.g. handler500.
from django.conf.urls.defaults import *

urlpatterns = patterns('jobs.views',
    url(r'^(?P<job_id>\d+)-[\w-]+/?$', 'show',    name='show_job'),
    url(r'^new/?$',                    'create',  name='create_job'),
    url(r'^my/?$',                     'my',      name='my_jobs'),
    url(r'^check/(?P<job_id>\d+)/?$',  'check',   name='check_job'),
    url(r'^edit/(?P<job_id>\d+)/?$',   'edit',    name='edit_job'),
    url(r'^delete/(?P<job_id>\d+)/?$', 'destroy', name='destroy_job'),
)
