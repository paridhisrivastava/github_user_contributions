from src import app

app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'

app.debug = True
app.run(host='127.0.0.1', port=80, debug=True)


# from flask import Flask
# from flask import Flask, flash, redirect, render_template, request, session, abort
# import os
#
# app = Flask(__name__)
#
#
# @app.route('/')
# def home():
#     if not session.get('logged_in'):
#         return render_template('login.html')
#     else:
#         return "Hello Boss!"
#
#
# @app.route('/login', methods=['POST'])
# def do_admin_login():
#     if request.form['password'] == 'password' and request.form['username'] == 'admin':
#         session['logged_in'] = True
#     else:
#         flash('wrong password!')
#     return home()
#
#
# if __name__ == "__main__":
#     app.secret_key = os.urandom(12)
#     app.run(debug=True, host='127.0.0.1', port=4000)