#!/usr/bin/python
import os

if __name__ != '__main__':
    virtenv = os.environ['OPENSHIFT_PYTHON_DIR'] + '/virtenv/'
    virtualenv = os.path.join(virtenv, 'bin/activate_this.py')
    try:
        execfile(virtualenv, dict(__file__=virtualenv))
    except IOError:
        pass

#
# IMPORTANT: Put any additional includes below this line.  If placed above this
# line, it's possible required libraries won't be in your searchable path
#

import webapp2
import jinja2

import re

##### Begin Udacity Code #####

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = True)

def render_str(template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)

class BaseHandler(webapp2.RequestHandler):
    def render(self, template, **kw):
        self.response.out.write(render_str(template, **kw))

    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)
        
##### End Udacity Code #####

class HelloWebapp2(BaseHandler):
    def get(self):
        self.write('Hello, webapp2!')
        
class Unit2Rot13(BaseHandler):
    def get(self):
        self.render('unit2rot13.html')
    def post(self):
        rotated = ''
        content = self.request.get('text')
        if content:
            rotated = content.encode('rot13')
        self.render('unit2rot13.html', text = rotated)

class Unit2Welcome(BaseHandler):
    def get(self):
        username = self.request.get('username')
        self.render('unit2signupwelcome.html', username=username)
        
class Unit2Signup(BaseHandler):
    def get(self):
        self.render('unit2signup.html')
    def post(self):
        failed = False;
        
        username = self.request.get('username')
        password = self.request.get('password')
        verify = self.request.get('verify')
        email = self.request.get('email')
        
        USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
        if not USER_RE.match(username): 
            failed = True
        
        PASS_RE = re.compile(r"^.{3,20}$")
        if not PASS_RE.match(username): 
            failed = True
        
        if password != verify:
            failed = True
        
        EMAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")
        if not EMAIL_RE.match(email): 
            failed = True
        
        if failed:
            self.render('unit2rot13.html', username=username, email=email)
        else:
            self.redirect('/unit2/welcome?username='+username)
        
application = webapp2.WSGIApplication([
    ('/', HelloWebapp2),
    ('/unit2/rot13', Unit2Rot13),
    ('/unit2/signup', Unit2Signup),
    ('/unit2/welcome', Unit2Welcome),
], debug=True)

def main():
    from paste import httpserver
    httpserver.serve(application, host='127.0.0.1', port='8080')

if __name__ == '__main__':
    main()