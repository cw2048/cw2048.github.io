from flask import Flask, render_template
from data import test_posts, post1, profiles
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
import database


app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "Cassandra": generate_password_hash("password"),
    "David" : generate_password_hash("password")
}


@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username


@app.route("/")
@auth.login_required
def feed():
    people = database.get_people()
    return render_template('feed.html', posts=test_posts, title="Home Page", user=auth.current_user(), people=people)


@app.route("/comments/<int:post_id>")
def comments(post_id):
    post = test_posts[post_id]
    return render_template('comments.html', title="Comments", post=post)


@app.route("/login")
def login():

    return render_template('login.html', title="Log in")


@app.route("/login/<int:profile_id>")
@auth.login_required
def profile(profile_id):
    profile = profiles[profile_id]
    return render_template('profile.html', title="Profile", profile=profile)


@app.route('/create', methods = ['POST'])
def create():
    return 'content was: ' + request.form['post-content']



if __name__ == '__main__':
    app.run()