import folder
from unittest impot TestCase

class functionTestCase(TestCase) #class subclass of TestCase
    """example of unit tests."""
    
    def test_function(self) #test_ "function name"
        assertEqual folder.function(2, 3) == 5 #unittest has special methods.

        #use python -m unittest NAME_OF_FILE runs all cases
