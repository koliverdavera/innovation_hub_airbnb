from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
# from data import Articles
from flask import Flask
from flask_mysqldb import MySQL
# from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from functools import wraps

app = Flask(__name__)

# Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'hub_db'
app.config['MYSQL_PASSWORD'] = '1208'
app.config['MYSQL_DB'] = 'hub_db'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
# init MYSQL
mysql = MySQL(app)


# Articles = Articles()

# Index
@app.route('/')
def index():
    return "Hello world!"


# User Register
@app.route('/register', methods=['GET', 'POST'])
def sign_up():
    # TODO: check user input
    username, password, email = request.json.get('username', ''), \
                                request.json.get('password', ''), request.json.get('email', '')

    if len(email) == 0 or len(password) == 0 or len(email) == 0:
        return 'Some credentials are missing.'

    cur = mysql.connection.cursor()

    cur.execute("INSERT INTO user(email, username, password) VALUES( %s, %s, %s)", (email, username, password))

    mysql.connection.commit()

    cur.close()

    return "success"


# User login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get Form Fields
        # username = request.form['username']
        # password_candidate = request.form['password']
        username, password_candidate = request.json.get('username', ''), request.json.get('password', '')

        # Create cursor
        cur = mysql.connection.cursor()

        # Get user by username
        result = cur.execute("SELECT * FROM user WHERE username = %s", [username])

        if result > 0:
            # Get stored hash
            data = cur.fetchone()
            password = data['password']
            username = data['username']

            # Compare Passwords
            if password_candidate == password:
                # Passed
                session['logged_in'] = True
                session['username'] = username

                # flash('You are now logged in', 'success')
                return 'You are now logged in', 'success'
            else:
                error = 'Invalid login'
                return render_template('login.html', error=error)
            # Close connection
            cur.close()
        else:
            error = 'Username not found'
            return render_template('login.html', error=error)

    return render_template('login.html')


# Check if user logged in
def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, Please login', 'danger')
            return redirect(url_for('login'))

    return wrap


# Logout
@app.route('/logout')
@is_logged_in
def logout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.debug = True
    app.secret_key = 'secret123'
    app.run(host='0.0.0.0', ssl_context="adhoc", port=8000)
