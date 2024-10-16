from flask_mail import Mail, Message
from flask import Flask

mail = Mail()

def init_mail(app):
    app.config['MAIL_SERVER'] = 'smtp.uiowa.edu'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = 'your-email@uiowa.edu'
    app.config['MAIL_PASSWORD'] = 'your-email-password'
    mail.init_app(app)

def send_email(subject, body, recipient):
    msg = Message(subject, sender='your-email@uiowa.edu', recipients=[recipient])
    msg.body = body
    mail.send(msg)