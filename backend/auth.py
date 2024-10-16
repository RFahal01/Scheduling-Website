from functools import wraps
from flask import session, redirect, url_for, flash

def check_password(password):
    return password in ['Hawk123', 'MyPassword']

def require_login(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'authenticated' not in session and 'admin_authenticated' not in session:
            flash('Please log in to access this page.')
            return redirect(url_for('index'))
        return f(*args, **kwargs)
    return decorated_function