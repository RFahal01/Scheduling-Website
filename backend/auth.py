'''
 from functools import wraps
from flask import session, redirect, url_for, flash

# Function to check if the provided password is valid
def check_password(password):
    # List of valid passwords
    valid_passwords = ['Hawk123', 'MyPassword']
    # Return True if the password is in the list of valid passwords
    return password in valid_passwords

# Decorator to require login for accessing certain routes
def require_login(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Check if the user is authenticated or admin authenticated
        if 'authenticated' not in session and 'admin_authenticated' not in session:
            # Flash a message if the user is not logged in
            flash('Please log in to access this page.')
            # Redirect to the index page
            return redirect(url_for('index'))
        # Call the original function if the user is authenticated
        return f(*args, **kwargs)
    return decorated_function
    '''