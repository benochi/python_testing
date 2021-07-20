from app import app
from flask import session
from unittest import TestCase

class FlaskTests(TestCase):
  
    def setUp(self): #must be camel case
        """Stuff to do before every test"""
        print("Setting up!")
    
    def tearDown(self):
        """Will run after every test method"""
        print("Tearing down!")
    
    def test_1(self):
        print("test 1 running!")
    
  #Will run in this order:
  setUp()
  test_1()
  tearDown()

  
  #if you want setUp and Teardown ONCE before ALL tests and ONCE AFTER all tests:
  
  @classmethod
  def setUpClass(cls):
      print("Inside setup class")
    
  @classmethod
  def tearDownClass(cls)
      print("inside teardown class")
