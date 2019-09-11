# coding=utf-8
import re
import string
import os
import jinja2
import webapp2
import hashlib
import hmac
from random import choice

template_dir=os.path.join(os.path.dirname(__file__))

jinja_env=jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=True)
SECRET="imsosecret"

class Handler(webapp2.RequestHandler):

    def write(self,*a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t=jinja_env.get_template(template)
        return t.render(params)

    def render(self,template, **kw):
        self.write(self.render_str(template,**kw))

class WebScalable(Handler):
    def get(self):
        return "hola"

class WebScalable2(Handler):
    def get(self):
        return self.render("/index.html")

app=webapp2.WSGIApplication([("/scalable/", WebScalable),("/scalabl", WebScalable2)],debug=True)