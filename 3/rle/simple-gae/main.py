import webapp2
from handlers import MainHandler, AddHandler, StudentInfoHandler

#Main entry point to our application
app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/add', AddHandler),
    ('/students/(\d+)', StudentInfoHandler),
], debug=True)
