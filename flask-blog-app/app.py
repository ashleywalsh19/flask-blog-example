import os
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "blogposts.db"))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

db = SQLAlchemy(app)

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template('home.html')

@app.route("/add_to_blog", methods=["GET", "POST"])
def add_to_blog():
    posts = {}
    if request.form:
        title = request.form.get("title")
        date = request.form.get("date")
        text = request.form.get("text")
        print(request.form)
        post = Post(title=title, date=date, text=text)
        db.session.add(post)
        db.session.commit()
    posts = Post.query.all()
    return render_template("add_to_blog.html", posts=posts)

@app.route("/blog")
def blog():    
    posts = {}
    posts = Post.query.all()
    return render_template("blog.html", posts=posts)

class Post(db.Model):
    title = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    date = db.Column(db.String(80), unique=False, nullable=True, primary_key=False)
    text = db.Column(db.String(800), unique=True, nullable=True, primary_key=False)

    def __repr__(self):
        return "<Title: {}, Date: {}, Text: {}>".format(self.title, self.date, self.text)
  
if __name__ == "__main__":
    app.run(debug=True)