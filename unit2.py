import re
from webapp_utils import BaseHandler

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
            self.render('unit2signup.html', username=username, email=email)
        else:
            self.redirect('/unit2/welcome?username='+username)

class Unit2FizzBuzz(BaseHandler):
    def get(self):
        self.render('unit2fizzbuzz.html')