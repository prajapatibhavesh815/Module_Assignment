# user.py
from flask import Blueprint, render_template

user_bp = Blueprint('user', __name__, template_folder='templates', static_folder='static')

@user_bp.route('/profile')
def profile():
    return render_template('profile47.html')

@user_bp.route('/settings')
def settings():
    return "User Settings Page"
