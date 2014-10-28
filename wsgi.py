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

import re
import webapp2

from webapp_utils import BaseHandler
from unit2 import *
from unit3 import *

class HelloWebapp2(BaseHandler):
    def get(self):
        self.write('Hello, webapp2!')

import re
        
application = webapp2.WSGIApplication([
    ('/', HelloWebapp2),
    ('/unit2/rot13', Unit2Rot13),
    ('/unit2/signup', Unit2Signup),
    ('/unit2/welcome', Unit2Welcome),
    ('/unit2/fizzbuzz', Unit2FizzBuzz),
    ('/unit3/blog', Unit3ViewBlog),
    ('/unit3/blog/(\d+)', Unit3ViewPost),
    ('/unit3/blog/newpost', Unit3NewBlogPost)
], debug=True)

def main():
    from paste import httpserver
    httpserver.serve(application, host='127.0.0.1', port='8080')

if __name__ == '__main__':
    main()