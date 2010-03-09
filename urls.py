# NOTE: Must import *, since Django looks for things here, e.g. handler500.
from django.conf.urls.defaults import *

# Load the citygoround application's URLs
urlpatterns = patterns('',
    url(r'^$',        'jobs.views.list',    name='list_jobs'),
    url(r'^about/?$', 'django.views.generic.simple.direct_to_template',
        {'template': 'about.html', 'extra_context': {'title': 'How it works'}}),
    url(r'^jobs/',    include('jobs.urls'))
)
