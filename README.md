# Flask OpenAI & Image Classification Project

This project provides an API for image classification using TensorFlow's EfficientNetV2 model and a chatbot powered by OpenAI GPT.

## Features
- Image classification with EfficientNetV2 to classify Gleason scores.
- Chatbot interface powered by OpenAI GPT for conversation and insights.

## Prerequisites
Before you begin, ensure you have the following installed:
- Python 3.8+
- `pip` for managing Python packages

## Setup Instructions

### 1. Create a Virtual Environment
It’s recommended to use a virtual environment to isolate the project’s dependencies.

#### For Linux/macOS:
Run the following commands in your terminal:

python3 -m venv venv  # Create a virtual environment named 'venv'
#### For Windows:
python -m venv venv  # Create a virtual environment named 'venv'

###2. Activate the Virtual Environment
After creating the virtual environment, activate it with the following commands:

####For Linux/macOS:
source venv/bin/activate  # Activate the virtual environment

###3. Install Required Packages
Once the virtual environment is activated, install the required packages by running:
pip install -r requirements.txt  # Install all dependencies listed in requirements.txt

###4. Run the Flask Application
Finally, run the Flask application with the --reload option to automatically restart the server when code changes are detected:

flask run --reload  # Start the Flask application

