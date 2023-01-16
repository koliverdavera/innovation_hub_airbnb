from flask import flash, redirect, url_for, session
from flask import request
from flask import Flask
from flask_cors import CORS
from flask_mysqldb import MySQL
from functools import wraps
from model.predictor import get_prediction

app = Flask(__name__)
Cors = CORS(app)
CORS(app, resources={r'/*': {'origins': '*'}}, CORS_SUPPORTS_CREDENTIALS=True)
app.config['CORS_HEADERS'] = 'Content-Type'

# Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'hub_db'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'hub_db'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
# init MYSQL
mysql = MySQL(app)


# Index
@app.route('/')
def index():
    return "Airbnb calculator"


# User Register
@app.route('/register', methods=['GET', 'POST'])
def sign_up():
    # TODO: check user input
    username = request.json["username"]
    email = request.json["email"]
    password = request.json["password"]

    if len(email) == 0 or len(password) == 0 or len(email) == 0:
        return 'Some credentials are missing.'

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO user(email, username, password) "
                "VALUES( %s, %s, %s)",
                (email, username, password))
    mysql.connection.commit()
    cur.close()
    return "success"


# User login
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.json["username"]
        password_candidate = request.json["password"]

        cur = mysql.connection.cursor()
        # Get user by username
        result = cur.execute("SELECT * FROM user "
                             "WHERE username = %s", [username])

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
                ret = 'You are now logged in'
            else:
                ret = 'Invalid password'
            # Close connection
            cur.close()
            return ret
        else:
            error = 'Username not found'
            return error


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


@app.route('/calculator', methods=['POST', 'GET'])
# @is_logged_in
def calculator() -> str:
    params = request.json
    prediction = get_prediction(params)
    return str(prediction)


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
    app.run(host='127.0.0.1', ssl_context="adhoc", port=1234)
