###############
### Imports ###
###############

from flask import Flask 
from flask import jsonify
from flask import request
from flask import render_template 
from lib.json import write_to_json_file, read_from_json_file
app = Flask(__name__)
blog_post_json_filename = 'blog_posts.json'

###################
### Page Routes ###
###################

@app.route('/')
def landing_page():
    return render_page( page='landing_page.html' )

@app.route('/about_us')
def about_us():
    return render_page( page='about_us.html', title='About Us' )

@app.route('/get_involved')
def get_involved():
    return render_page( page='get_involved.html' )

@app.route('/blog_post', methods=['GET', 'POST', 'DELETE'])
def blog_post():
    if request.method == 'GET':
        # Return the json in the file
        return jsonify( read_from_json_file( blog_post_json_filename ) )

    elif request.method == 'POST':
        # Grab params for the new blog post
        post_title = request.args['post_title']
        post_body  = request.args['post_body']
        new_data = {
            'post_title' : post_title,
            'post_body'  : post_body,
        }

        # Grab the current blog posts and put our new one at the 
        # front of the array. We do this because we want the newest blog 
        # post to be at the front/top/etc
        data = read_from_json_file( blog_post_json_filename )
        data.insert( 0, new_data )

        # Write our updated data to the blog posts json file
        write_to_json_file( blog_post_json_filename, data )
        
        # Return the json in the file
        return jsonify( read_from_json_file( blog_post_json_filename ) )

    elif request.method == 'DELETE':
        # Grab the title of the post that we want to delete
        post_title = request.args['post_title']

        # Grab the current blog posts
        data = read_from_json_file( blog_post_json_filename )

        # Find the index of the post that we want to delete
        for index, post in enumerate( data ):
            if post['post_title'] == post_title:
                index_to_delete = index
                break

        # If we found it then delete it
        if index_to_delete is not None:
            del data[index_to_delete]

        # Write our new set of blog posts to the json file
        write_to_json_file( blog_post_json_filename, data )

        # Return the new set of json files that are saved in the json file
        return jsonify( read_from_json_file( blog_post_json_filename ) )

    else:
        raise Exception( 'Wrong method for route' )

    

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

