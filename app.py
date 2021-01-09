###############
### Imports ###
###############

from flask import Flask
from flask import render_template 
app = Flask(__name__)

##############
### Routes ###
##############

# NOTE: We always render the page_base.html template and then pass in the page we want to 
# render. This is cleaner and keeps repeated code out of the individual page templates.

@app.route('/')
def landing_page():
    return render_template( 'page_base.html', page='landing_page.html' );

@app.route('/about_us')
def about_us():
    return render_template( 'page_base.html', page='about_us.html', title='About Us' );

if __name__ == '__main__':
    app.run()

