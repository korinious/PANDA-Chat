# Import necessary libraries and modules
from flask import Flask, render_template
from flask_restful import Api
from .routes.chat import Chat  # Import Chat resource for handling chat-related requests
from .routes.upload import UploadImage  # Import UploadImage resource for handling image uploads

# Initialize the Flask application
app = Flask(__name__)
# Initialize the Flask-RESTful API
api = Api(app)

# Route to render the index.html template when accessing the root URL
@app.route('/')
def index():
    """
    Render the index page.

    Returns:
        str: Rendered HTML content of the index page.
    """
    return render_template('index.html')

# Add RESTful resources to the API with their corresponding routes
api.add_resource(UploadImage, '/upload')  # Route for uploading images
api.add_resource(Chat, '/get_response')  # Route for getting chat responses

# Run the application
if __name__ == "__main__":
    """
    Start the Flask application.

    The app runs in debug mode, which provides detailed error messages 
    and automatically reloads the server on code changes.
    """
    app.run(debug=True, host="0.0.0.0", port=8000)
