#!/usr/bin/env python

import os
import webapp2
import jinja2

from models import Student

#Here we create jinja2 environment. Don't bother about this for now
template_loader = jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates'))
jinja2_env = jinja2.Environment(loader=template_loader)

class MainHandler(webapp2.RequestHandler):
    '''This handler will respond to GET requests and return response with
    a list of currently added student records and a form to add new student.

    '''
    def get(self):
        '''This function is called when GET request is routed to this handler.

        '''
        #Retrieve all Student entities from datastore
        #Remember, this returns so-called cursor, not a list of entities
        students = Student.all()
        #Loading template
        tpl = jinja2_env.get_template('main.html')
        #Creating the context, which will be used to fill template
        render_context = {'students': students} if students.count() != 0 else {}
        #Rendering template
        result = tpl.render(render_context)
        #Sending response
        self.response.write(result)

class AddHandler(webapp2.RequestHandler):
    '''This handler will respond to POST request, when new student record is added.

    '''
    def post(self):
        '''This function is called when POST request is routed to this handler.

        '''
        #Get name and group from HTTP request
        name = self.request.get('name')
        group = self.request.get('group')
        #Create new Student entity
        student = Student(name=name, group=group)
        #Save it
        student.put()
        #Redirect to home page
        self.redirect('/')

class StudentInfoHandler(webapp2.RequestHandler):
    '''This handler returns student info on a separate page. Supports
    only GET requests.

    '''
    def get(self, student_id):
        #TODO: Put your code here
        #Below is stub code
        tpl = jinja2_env.get_template('student.html')
        render_context = {}
        result = tpl.render(render_context)
        self.response.write(result)