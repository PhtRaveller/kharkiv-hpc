import webapp2
from handlers import MainHandler, AddHandler

#Main entry point to our application
app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/add', AddHandler),
], debug=True)
