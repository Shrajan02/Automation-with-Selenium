from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# User database
users = {
    'user1': 'pass1',
    'user2': 'pass2',
}

# Login page
@app.route('/')
def login():
    return render_template('login.html')

# Signup page
@app.route('/signup')
def signup():
    return render_template('signup.html')

# Signup form submission
@app.route('/signup', methods=['POST'])
def signup_submit():
    username = request.form['username']
    password = request.form['password']
    confirm_password = request.form['confirm_password']

    # Check if username already exists
    if username in users:
        return render_template('signup.html', error='Username already exists')

    # Check if password meets requirements
    if len(password) < 8:
        return render_template('signup.html', error='Password must be at least 8 characters long')

    # Check if password and confirm password match
    if password != confirm_password:
        return render_template('signup.html', error='Passwords do not match')

    # Add user to database
    users[username] = password

    return redirect(url_for('login'))

# Login form submission
@app.route('/', methods=['POST'])
def login_submit():
    username = request.form['username']
    password = request.form['password']

    # Check if username exists
    if username not in users:
        return render_template('login.html', error='Invalid username or password')

    # Check if password is correct
    if users[username] != password:
        return render_template('login.html', error='Invalid username or password')

    return 'Logged in successfully'

if __name__ == '__main__':
    app.run(debug=True)