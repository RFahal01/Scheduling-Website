from flask import Flask, render_template
from routes import setup_routes

# Initialize the Flask application
app = Flask(__name__)

# Set the secret key for session management
app.secret_key = 'your_secret_key'

# Setup routes for the application
setup_routes(app)

# Main entry point of the application
if __name__ == '__main__':
    # Run the application in debug mode on all available IP addresses and port 5000
    app.run(debug=True, host='0.0.0.0', port=5000)