import webapp2
import jinja2
import time
import logging
import datetime
import json as simplejson
from session import session
from config.settings import project_info
from functions import helpers as h

# jinja env
jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader('application/static/templates/'), autoescape=True)

class BaseHandler(webapp2.RequestHandler):
    def __init__(self, request=None, response=None):
        self.initialize(request, response)
        
        self.tv = {} # Global

        self.now = datetime.datetime.now()
        self.session = session.get_session()
        self.user = session.get_current_user(self.session)

    def render(self, template_path=None, force=False):
        self.tv["user"] = self.user
        self.tv["current_timestamp"] = time.mktime(self.now.timetuple())
        self.tv["current_url"] = self.request.uri
        self.tv["proj_info"] = project_info # project details

        this_cookies = self.request.headers.get("Cookie")
        if this_cookies:
            cookies = h.get_cookies(this_cookies)
            if "error" in cookies:
                self.tv["error"] = cookies["error"]

        template = jinja_environment.get_template(template_path)
        self.response.out.write(template.render(self.tv))

    def logged_this_user(self, user):
        session.login(user)

    def logout(self):
        if self.session.is_active():
            self.session.terminate()


    def set_error_cookie(self, error):
        expiry = datetime.datetime.now() + datetime.timedelta(seconds=5)
        self.response.set_cookie('error', error, expires=expiry)
        return True






