from flask import Flask, render_template, redirect, url_for, flash, session
from config import Config
from forms import RegistrationForm, LoginForm
from models import create_user, get_user_by_email, bcrypt

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def home():
    return render_template('home49.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():
        create_user(form.username.data, form.email.data, form.password.data)
        flash('Account created successfully!', 'success')
        return redirect(url_for('login'))
    return render_template('signup.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = get_user_by_email(form.email.data)
        if user and bcrypt.check_password_hash(user['password'], form.password.data):
            session['user_id'] = str(user['_id'])
            session['username'] = user['username']
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Login unsuccessful. Please check your email and password', 'danger')
    return render_template('login49.html', form=form)

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return f"Hello, {session['username']}! Welcome to Geeks"
    else:
        flash('Please login to access this page', 'danger')
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run()
