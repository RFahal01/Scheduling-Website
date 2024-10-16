from flask import Flask, render_template
from routes import setup_routes

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Setup routes
setup_routes(app)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)