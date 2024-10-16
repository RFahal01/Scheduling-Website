from flask import render_template, request, redirect, url_for, session, flash
from auth import check_password, require_login
from utils import send_email

def setup_routes(app):
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/login', methods=['POST'])
    def login():
        password = request.form.get('password')
        if password == 'Hawk123':
            session['authenticated'] = True
            return redirect(url_for('calendar'))
        elif password == 'MyPassword':
            session['admin_authenticated'] = True
            return redirect(url_for('announcements'))
        else:
            flash('Invalid password.')
            return redirect(url_for('index'))

    @app.route('/calendar')
    @require_login
    def calendar():
        return render_template('calendar.html')

    @app.route('/announcements')
    @require_login
    def announcements():
        return render_template('announcements.html')

    @app.route('/edit_announcements', methods=['GET', 'POST'])
    def edit_announcements():
        if 'admin_authenticated' not in session:
            return redirect(url_for('index'))
        if request.method == 'POST':
            # Handle announcement editing
            new_announcement = request.form.get('announcement')
            flash('Announcement updated successfully.')
            return redirect(url_for('announcements'))
        return render_template('edit_announcements.html')

    @app.route('/add_shift', methods=['POST'])
    @require_login
    def add_shift():
        shift_details = request.form
        send_email('Shift Added', f'Shift added: {shift_details}', 'rfahal@uiowa.edu')
        flash('Shift added successfully.')
        return redirect(url_for('calendar'))

    @app.route('/delete_shift', methods=['POST'])
    @require_login
    def delete_shift():
        shift_id = request.form.get('shift_id')
        send_email('Shift Deleted', f'Shift {shift_id} deleted', 'rfahal@uiowa.edu')
        flash('Shift deleted successfully.')
        return redirect(url_for('calendar'))