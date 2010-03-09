from google.appengine.ext import db
from datetime import datetime
from hashlib import md5
import re

class Job(db.Model):
    title = db.StringProperty(required=True, indexed=False)
    description = db.TextProperty(required=True)
    url = db.StringProperty(indexed=False)
    hackernews_login = db.StringProperty(required=True, indexed=False)
    code = db.StringProperty(required=True, indexed=False)
    status = db.StringProperty(required=True, choices=['unchecked', 'queued', 'failed', 'published'], default='unchecked')
    owner = db.UserProperty(required=True, auto_current_user_add=True)
    created_at = db.DateTimeProperty(required=True, auto_now_add=True)
    queued_at = db.DateTimeProperty()
    published_at = db.DateTimeProperty()

    def __init__(self, *args, **kwargs):
        if 'code' not in kwargs: # when we create new job
            kwargs['code'] = md5(datetime.now().isoformat()).hexdigest()[0:4] # generate random 4-symbol code
        super(Job, self).__init__(*args, **kwargs)

    _attribute_pattern = re.compile('^is_(published|queued|failed)$')
    def __getattr__(self, name):
        matched_name = self._attribute_pattern.match(name)
        if matched_name:
            return self.status == matched_name.group(1) # 3 attributes to check for 3 statuses
        else:
            raise AttributeError

    def publish(self):
        self.status = 'published'
        self.published_at = datetime.now()

    def queue(self):
        self.status = 'queued'
        self.queued_at = datetime.now()

    def owned_by(self, current_user, is_current_user_admin):
        return (current_user and self.owner.user_id() == current_user.user_id()) or is_current_user_admin

    def owner_profile_url(self):
        return "http://news.ycombinator.com/user?id=%s" % (self.hackernews_login,)
