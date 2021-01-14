# IF the blog posts json file doesnt yet exist then generate it and make it an empty array
# However if it already exists then don't touch it
if ! test -f blog_posts.json; then
    echo "Generating blog posts json file..."
    touch blog_posts.json
    echo "[]" >> blog_posts.json
    echo "Blog posts json file generated!"
else
    echo "Skipping blog posts json file generation..."
fi

echo "Starting flask server..."
FLASK_APP=app.py FLASK_ENV=development flask run
