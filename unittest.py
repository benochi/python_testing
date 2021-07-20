import folder
from unittest import TestCase

class FunctionTestCase(TestCase) #class subclass of TestCase
    """example of unit tests."""
    
    def test_function(self) #test_ "function name"
        self.assertEqual(folder.function(2, 3), 5) #unittest has special methods. NOTE 2 args with this method. 
        self.assertEqual(folder.function(2, 4), 6)
        self.assertEqual(folder.function(-2, -3), -5)
    
    def test_function2(self):
        assert folder.function(2, 3) == 5 #wouldn't normally use assert, but for syntax. 
        #use python -m unittest NAME_OF_FILE runs all cases

        
    from app import app
    from unittest import TestCase
    
    class ColorViewsTestCase(TestCase):
        def test_color_form(self):
            with app.test_client() as client:#client refers to server
                res = client.get('/')
                html = res.get_data(as_Text=True)
                
                self.assertEqual(res.status_code, 200) #checks response code for 200
                self.assertIn('<h1>Color Form</h1>', html) #checks response data string for this phrase, html is just variable name
                
        def test_redirection(self):
            with app.test_client() as client:
                res = client.get('/redirect-me')
                
                self.assertEqual(res.status_code, 302)
                self.assertEqual(res.location, 'http://localhost/') #don't need /loclahost/5000 for example. 
        
        def test_redirection_followed(self):
            with app.tesst_client() as client:
                res = client.get('rediect-me', follow_redirects=True)
                html = res.get_data(as_text=True)
                
                self.assertEqual(res.statuscode, 200)
                self.assertIn('<h1>Color Form</h1>', html)
