###############
### Imports ###
###############

from flask import Flask
from flask import render_template 
app = Flask(__name__)

##############
### Routes ###
##############

@app.route('/')
def landing_page():
    return render_page( page='landing_page.html' )

@app.route('/about_us')
def about_us():
    return render_page( page='about_us.html', title='About Us' )

######################
### Util Functions ###
######################

# We always render the page_base.html template and then pass in the page we want to 
# render. This is cleaner and keeps repeated code out of the individual page templates.
def render_page( **args ):

    # Check that we have our required arguments
    if( 'page' not in args):
        raise Exception( 'Page was not passed to render_page function' )

    # Pass those params to the render_template function along with our page_base.html template.
    return render_template( 'page_base.html', **args )

if __name__ == '__main__':
    app.run()

