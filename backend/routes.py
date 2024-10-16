from flask import render_template, request, redirect, url_for, session, flash
from utils import send_email

def setup_routes(app):
    @app.route('/')
    def index():
        # Render the index page for users to enter the website
        return render_template('index.html')

    @app.route('/calendar')
    def calendar():
        # Render the calendar page for all users
        return render_template('calendar.html')

    @app.route('/announcements')
    def announcements():
        # Render the announcements page for all users
        return render_template('announcements.html')

    @app.route('/edit_announcements', methods=['GET', 'POST'])
    def edit_announcements():
        # Render edit page or process editing announcements
        if request.method == 'POST':
            new_announcement = request.form.get('announcement')
            flash('Announcement updated successfully.')
            return redirect(url_for('announcements'))
        return render_template('edit_announcements.html')

    @app.route('/add_shift', methods=['POST'])
    def add_shift():
        # Get shift details from the form
        shift_details = request.form
        # Send an email notification for the added shift
        send_email('Shift Added', f'Shift added: {shift_details}', 'rfahal@uiowa.edu')
        flash('Shift added successfully.')
        return redirect(url_for('calendar'))

    @app.route('/delete_shift', methods=['POST'])
    def delete_shift():
        # Get the shift ID from the form
        shift_id = request.form.get('shift_id')
        # Send an email notification for the deleted shift
        send_email('Shift Deleted', f'Shift {shift_id} deleted', 'rfahal@uiowa.edu')
        flash('Shift deleted successfully.')
        return redirect(url_for('calendar'))