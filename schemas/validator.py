# app/utils/validators.py

from flask import request  # Import request to access incoming data
from marshmallow import Schema, fields, ValidationError  # Import Schema, fields, and ValidationError from Marshmallow for validation

class ImageUploadSchema(Schema):
    """
    Schema for validating image uploads.
    """
    file = fields.Field(required=True)  # Define a required field for the uploaded image file

class ChatMessageSchema(Schema):
    """
    Schema for validating chat messages.
    """
    message = fields.String(required=True)  # Define a required string field for the chat message

def validate_image_upload():
    """
    Validate the uploaded image file.

    Returns:
        dict: Error message if validation fails; None if successful.
    """
    schema = ImageUploadSchema()  # Instantiate the image upload schema
    try:
        schema.load(request.files)  # Validate the incoming files
    except ValidationError as err:  # Catch validation errors
        return {'error': err.messages}, 400  # Return error messages with a 400 status code

def validate_chat_message():
    """
    Validate the chat message payload.

    Returns:
        dict: Error message if validation fails; None if successful.
    """
    schema = ChatMessageSchema()  # Instantiate the chat message schema
    try:
        schema.load(request.json)  # Validate the incoming JSON data
    except ValidationError as err:  # Catch validation errors
        return {'error': err.messages}, 400  # Return error messages with
