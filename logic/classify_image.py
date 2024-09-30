from ..models.image_model import image_classification_model # Import the pre-trained image classification model
import tensorflow as tf  # Import TensorFlow for image processing and model predictions

def classify_image(image) -> list:
    """
    Classifies the input image using the pre-trained image classification model.

    Parameters:
    - image: A TensorFlow tensor representing the input image to be classified.

    Returns:
    - A list of predictions from the model.
    """
    
    # Resize the input image to the required dimensions for the model
    image = tf.image.resize(image, (128, 128))
    
    # Expand dimensions to add a batch size of 1 (the model expects a batch of images)
    image = tf.expand_dims(image, 0)
   
    # Make predictions using the pre-trained model
    predictions = image_classification_model.predict(image)
    
    # Return the predictions made by the model
    return predictions
