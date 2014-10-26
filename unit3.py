import re
from dbconnect import db, cur
from webapp_utils import BaseHandler

class Unit3ViewBlog(BaseHandler):
    def get(self):
        cur.execute("SELECT * FROM BLOG_POSTS ORDER BY TIMESTAMP DESC")
        self.render('unit3viewblog.html', posts=cur.fetchall())

class Unit3NewBlogPost(BaseHandler):
    def saveNewPost(self, subject, content):
        cur.execute("INSERT INTO blog_posts (SUBJECT, CONTENT) VALUES ('%s', '%s')"
                        %(subject, content))
        db.commit()
        
    def get(self):
        self.render('unit3newblogpost.html')

    def post(self):
        subject = self.request.get('subject')
        content = self.request.get('content')
        
        self.saveNewPost(subject, content)
        
        self.redirect('/unit3/blog')