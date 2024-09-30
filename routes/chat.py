# app/routes/chat_routes.py

from flask import request  # Import request to handle incoming requests
from flask_restful import Resource  # Import Resource for creating RESTful resources
from ..schemas.validator import validate_chat_message  # Import the chat message validation function
from ..services.chat_service import chat_with_ai  # Import the function to get AI responses

class Chat(Resource):
    """
    Chat Resource for handling user messages and returning AI responses.
    """

    def post(self):
        """
        Handle POST requests to the chat endpoint.

        This method validates the incoming chat message, processes it, and
        returns an AI-generated response.

        Returns:
            dict: A dictionary containing the AI response or an error message if validation fails.
        """
        
        # Validate the incoming chat message using the validation schema
        validation_result = validate_chat_message()
        if validation_result:  # If validation fails
            return validation_result  # Return the validation error response
        
        # Retrieve the JSON data from the request
        data = request.json
        user_message = data.get('message')  # Extract the user's message from the JSON
        
        # Get the AI response based on the user's message
        ai_response = chat_with_ai(user_message)
        
        # Return the AI response in a JSON format
        return {'response': ai_response}
