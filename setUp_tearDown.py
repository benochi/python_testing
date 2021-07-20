class FlaskTests(TestCase):
  
  def setUp(self): #must be camel case
    """Stuff to do before every test"""
    
  def tearDown(self):
    """Will run after every test method"""
    
  def test_1(self):
    ...
    
  #Will run as...
  setUp()
  test_1()
  tearDown()
