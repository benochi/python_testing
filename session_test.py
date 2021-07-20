from app import app
from flask import session #make sure to import session for testing. 
from unittest import TestCase


def test_session_count(self):
    with app.test_client() as client:
        res = client.get('/')
    
        self.assertEqual(res.status_code, 200)
        self.assertEqual(session['count'], 1) #each test client starts from scratch
  
  
#This can be used to check for usernames or more complex input. 
def test_session_count_set(self):
    with app.test_client() as client:
        #Any changes to session should go here
        with client.session_transaction() as change_session: #change_session is variable
            change_session['count'] = 999
        #Now those changes will be in Flask's 'session'
        res = client.get('/')
    
    
        self.assertEqual(res.status_code, 200)
        self.assertEqual(session['count'], 1000) #checks that session Of count == 1000
