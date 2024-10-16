from flask import Flask, render_template, request, redirect, url_for, session, flash
from auth import check_password, require_login
from utils import send_email

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def setup_routes(app):
    @app.route('/', methods=['GET', 'POST'])
    def index():
        if request.method == 'POST':
            # Process the login form
            password = request.form.get('password')
            # Check if the password matches 'Hawk123'
            if password == 'Hawk123':
                session['authenticated'] = True
                # Redirect to the calendar page if authenticated
                return redirect(url_for('calendar'))
            # Check if the password matches 'MyPassword'
            elif password == 'MyPassword':
                session['admin_authenticated'] = True
                # Redirect to the announcements page if admin authenticated
                return redirect(url_for('announcements'))
            else:
                # Flash an error message if the password is invalid
                flash('Invalid password.')
                return redirect(url_for('index'))
        # Render the login page for GET requests
        return render_template('index.html')

    @app.route('/calendar')
    @require_login
    def calendar():
        # Render the calendar page if the user is authenticated
        return render_template('calendar.html')

    @app.route('/announcements')
    @require_login
    def announcements():
        # Render the announcements page if the user is admin authenticated
        return render_template('announcements.html')

    @app.route('/edit_announcements', methods=['GET', 'POST'])
    @require_login
    def edit_announcements():
        # Check if the user is admin authenticated
        if 'admin_authenticated' not in session:
            return redirect(url_for('index'))
        if request.method == 'POST':
            # Handle announcement editing
            new_announcement = request.form.get('announcement')
            flash('Announcement updated successfully.')
            return redirect(url_for('announcements'))
        # Render the edit announcements page
        return render_template('edit_announcements.html')

    @app.route('/add_shift', methods=['POST'])
    @require_login
    def add_shift():
        # Get shift details from the form
        shift_details = request.form
        # Send an email notification for the added shift
        send_email('Shift Added', f'Shift added: {shift_details}', 'rfahal@uiowa.edu')
        flash('Shift added successfully.')
        # Redirect to the calendar page
        return redirect(url_for('calendar'))

    @app.route('/delete_shift', methods=['POST'])
    @require_login
    def delete_shift():
        # Get the shift ID from the form
        shift_id = request.form.get('shift_id')
        # Send an email notification for the deleted shift
        send_email('Shift Deleted', f'Shift {shift_id} deleted', 'rfahal@uiowa.edu')
        flash('Shift deleted successfully.')
        # Redirect to the calendar page
        return redirect(url_for('calendar'))

if __name__ == '__main__':
    setup_routes(app)
    app.run(debug=True)
