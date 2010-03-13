from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import urlfetch
from jobs.models import Job

import sys
for k in [k for k in sys.modules if k.startswith('django')]:
    del sys.modules[k]
# workaround above is to prevent UnacceptableVersionError exception
from google.appengine.dist import use_library
use_library('django', '1.1')

class CheckQueuedJobsHandler(webapp.RequestHandler):
    def get(self):
        job = Job.all().filter('status =', 'queued').order('queued_at').fetch(1)
        if job:
            job = job[0] # fetch() returns list of items
            result = urlfetch.fetch(job.owner_profile_url)
            if result.status_code == 200:
                try: # if owner's profile contents code, this will pass silently
                    result.content.index(job.code)
                    job.publish()
                    job.put()
                    self.response.out.write('Published')
                    return 
                except ValueError:
                    pass
            job.fail()
            job.put()
            self.response.out.write('Failed')
            return 
        else:
            self.response.out.write('No queued jobs.')

class RssHandler(webapp.RequestHandler):
    def get(self):
        jobs = Job.all().filter('status =', 'published').order('-published_at').fetch(20)
        pub_date = None
        self.response.headers['Content-Type'] = 'application/rss+xml'
        self.response.out.write(template.render('templates/rss.xml',
                                                {'jobs': jobs,
                                                 'host': self.request.headers.get('host'),
                                                 'pub_date': pub_date}))

application = webapp.WSGIApplication([('/check_queued_jobs', CheckQueuedJobsHandler),
                                      ('/rss', RssHandler)],
                                     debug = True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
