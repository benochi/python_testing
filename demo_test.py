import folder
from unittest impot TestCase

class functionTestCase(TestCase) #class subclass of TestCase
    """example of unit tests."""
    
    def test_function(self) #test_ "function name"
        assert folder.function(2, 3) == 5
