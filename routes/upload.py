# app/routes/image_routes.py

from flask import request  # Import request to handle incoming requests
from flask_restful import Resource  # Import Resource for creating RESTful resources
import tensorflow as tf  # Import TensorFlow for image processing and model predictions
import numpy as np  # Import NumPy for numerical operationss
from ..logic.classify_image import classify_image  # Import the function that handles image classification logic
from ..services.chat_service import chat_with_ai  # Import the function to interact with AI for responses
from ..schemas.validator import validate_image_upload  # Import the image upload validation function

class UploadImage(Resource):
    """
    UploadImage Resource for handling image uploads and predictions.
    """

    def post(self):
        """
        Handle POST requests to the image upload endpoint.

        This method validates the uploaded image, processes it to get predictions,
        and returns both the predictions and an AI-generated response.

        Returns:
            dict: A dictionary containing the predictions and AI response, or an error message if validation fails.
        """
        
        # Validate the incoming image upload using the validation schema
        validation_result = validate_image_upload()
        if validation_result:  # If validation fails
            return validation_result  # Return the validation error response
        
    
        # Retrieve the uploaded file from the request
        file = request.files['file']  # Access the uploaded file
        image_data = file.read()  # Read the image data from the file
        image = tf.image.decode_image(image_data, channels=3)  # Decode the image data into a TensorFlow tensor

        # Classify the image using the logic defined in a separate module
        predictions = classify_image(image)  # Call the image classification function
        score = np.argmax(predictions)  # Get the index of the highest prediction score

        # Mapping of score indices to descriptive text
        score_mapping = {
            0: "ISUP scores equals 0: background (non-tissue) or unknown",
            1: "ISUP scores equals 1: stroma (connective tissue, non-epithelial tissue)",
            2: "ISUP scores equals 2: healthy (benign) epithelium",
            3: "ISUP scores equals 3: cancerous epithelium",
            4: "ISUP scores equals 4: cancerous epithelium",
            5: "ISUP scores equals 5: cancerous epithelium"
        }

        # Retrieve the prediction description based on the score
        result = score_mapping.get(score, "Unknown score")  # Get the corresponding result description

        # Generate an AI response based on the prediction result
        ai_response = chat_with_ai(f"The model predicted the following values: {result}")

        # Return the predictions and AI response in JSON format
        return {'predictions': result, 'response': ai_response}

    
        return {'error': f"Error processing image: {str(e)}"}, 500  # Return an error message with a 500 status code
