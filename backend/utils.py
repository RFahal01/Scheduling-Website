from flask_mail import Mail, Message
from flask import Flask

# Initialize the Mail object
mail = Mail()

def init_mail(app):
    """
    Initialize the mail settings for the Flask application.
    
    :param app: Flask application instance
    """
    # Mail server configuration
    app.config['MAIL_SERVER'] = 'smtp.uiowa.edu'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = 'your-email@uiowa.edu'
    app.config['MAIL_PASSWORD'] = 'your-email-password'
    
    # Initialize the mail object with the app configuration
    mail.init_app(app)

def send_email(subject, body, recipient):
    """
    Send an email using the configured mail settings.
    
    :param subject: Subject of the email
    :param body: Body of the email
    :param recipient: Recipient email address
    """
    # Create a new Message object
    msg = Message(subject, sender='your-email@uiowa.edu', recipients=[recipient])
    msg.body = body
    
    # Send the email
    mail.send(msg)