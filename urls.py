# NOTE: Must import *, since Django looks for things here, e.g. handler500.
from django.conf.urls.defaults import *

# Load the citygoround application's URLs
urlpatterns = patterns('',
    url(r'',     'jobs.views.list',    name='list_jobs'),
    url(r'^jobs/', include('jobs.urls'))
)
