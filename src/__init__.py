import os
from flask import Flask, render_template, session, request, flash, redirect, url_for, abort
from flask_restful import Api, Resource
import markdown
from src.github_user import GithubUser


app = Flask(__name__, template_folder='templates')
api = Api(app)

username = ''
password = ''


@app.route("/")
def index():
    with open(os.path.dirname(app.root_path) +
              '/README.md', 'r') as rdme_file:
        content = rdme_file.read()

    return markdown.markdown(content)


@app.route('/login')
def home():
    session['logged_in'] = False
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def do_admin_login():
    global username, password
    if request.form['password'] is None or request.form['username'] is None:
        flash('wrong password!')
        abort(400)
    session['logged_in'] = True
    username = request.form['username']
    password = request.form['password']
    # return redirect(url_for('user/', username=request.form['username']))
    return redirect('user', code=307)


class UserResource(Resource):
    user = None

    def post(self):
        print(username, password)
        self.user = GithubUser(username, password)
        session['logged_in'] = True

    def get(self):
        print(self.user.username, self.user.password)


api.add_resource(UserResource, '/user')