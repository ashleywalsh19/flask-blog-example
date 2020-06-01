# flask-blog-app
Building an elementary blog with Flask/SQL

## Getting Started
Clone into the directory and cd into the flask-blog-app directory. Run `python app.py` from inside the directory and navigate to the locally hosted website -- you may need to `pip install flask sqlalchemy flask-sqlalchemy` to quiet any dependency errors

## Resetting/Creating a new SQL database
You can reset the database (i.e. clear the blog of all posts) by deleting the 'blogposts.db' file in the directory. Recreate a (empty) database by opening a Python shell (type `python` then ENTER in your terminal) and do the following:

 `from bookmanager import db`
 
`db.create_all()`

`exit()`

This will create a new, empty database for all your blog entries.

## Adding a post to your database

The website has a "hidden" app route, that is 'localhost:5000/add_to_blog'. There, you can enter a blog post (title, date, and of course the text content) and when you nevigate back to the 'Blog' tab you will see your update reflected there!

## Sources
https://www.codementor.io/@garethdwyer/building-a-crud-application-with-flask-and-sqlalchemy-dm3wv7yu2
https://www.w3schools.com/howto/howto_css_blog_layout.asp
https://www.freecodecamp.org/news/how-to-build-a-web-application-using-flask-and-deploy-it-to-the-cloud-3551c985e492/
