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
