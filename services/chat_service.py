# Import necessary configurations for OpenAI
from ..config.settings import openai, MODEL_NAME, MODEL_PARAMS

# Initialize an empty list to keep track of the conversation history
conversation_history = []

def chat_with_ai(user_message: str) -> str:
    """
    Interact with the OpenAI GPT model to generate a response.

    Args:
        user_message (str): The message from the user to be processed.

    Returns:
        str: The AI-generated response or an error message.
    """
    try:
        # Define a concise system message to guide the AI's behavior
        system_message = (
            "You are an AI expert on machine learning models and prostate cancer datasets. "
            "Provide concise responses (20 words max) and always end with a question to engage the user. "
            "You interpret ISUP scores as follows:\n"
            "0: Background (non-tissue) or unknown\n"
            "1: Stroma (connective tissue, non-epithelial)\n"
            "2: Healthy (benign) epithelium\n"
            "3: Cancerous epithelium (ISUP  3)\n"
            "4: Cancerous epithelium (ISUP 4)\n"
            "5: Cancerous epithelium (ISUP 5)\n"
            "The model generates scores based on uploaded images, so when users inquire about an image, they refer to the predicted score. "
            "Encourage active conversation and suggest next steps or related insights."
        )


        # Initialize the conversation with the system message if it's the first interaction
        if not conversation_history:
            conversation_history.append({'role': 'system', 'content': system_message})

        # Append the user's message to the conversation history
        conversation_history.append({'role': 'user', 'content': user_message})

        # Create a chat completion request to OpenAI
        response = openai.ChatCompletion.create(
            model=MODEL_NAME,  # Specify the model to use
            messages=conversation_history,  # Pass the conversation history
            **MODEL_PARAMS  # Include additional parameters for the model
        )

        # Extract the AI's response from the API response
        ai_response = response.choices[0].message['content']

        # Append the AI's response to the conversation history
        conversation_history.append({'role': 'assistant', 'content': ai_response})

        return ai_response  # Return the AI's response

    except Exception as e:
        # Return an error message if an exception occurs
        return f"Error: {str(e)}"
