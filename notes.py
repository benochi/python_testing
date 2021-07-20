#add before test case classes

#make Flask errors be python errors instead of HTML error pages.
app.config['TESTING'] = True

#Do this if using debug toolbar, bit of hack
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']
