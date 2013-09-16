from google.appengine.ext import db

class Student(db.Model):
    '''Model for student entities
    '''
    name = db.StringProperty(required=True) #student's name
    group = db.StringProperty(required=True) #student's group
    added = db.DateTimeProperty(auto_now_add=True) #date, when record added