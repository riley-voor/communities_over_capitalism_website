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
def index():
    return render_template( 'index.html' );

if __name__ == '__main__':
    app.run()

