#add before test case classes

#make Flask errors be python errors instead of HTML error pages.
app.config['TESTING'] = True

#Do this if using debug toolbar, bit of hack
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']
#debug toolbar will mess up testing when using html = res.get_data(at_text=True)
#debug toolbar also INTERCEPTS REDIRECTS by default and will change status codes. 


#python -m unittest
#python -m unittest tests_name
#python -m unittest tests_name.NameViewTestCase
#python -m unittest tests_name.NameTestCase.test_method 
#files/cases/methods
