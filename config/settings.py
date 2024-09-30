import openai  # Import the OpenAI library to interact with the GPT models

# OpenAI configuration
openai.api_key = "***************************************************"
# Set the API key to authenticate requests to the OpenAI API.
# **Important:** Do not expose your API key in public repositories.

MODEL_NAME = "gpt-4o"  # Specify the model name to be used for generating responses.

# Define model parameters for API calls
MODEL_PARAMS = {
    "temperature": 0.5,  # Controls the randomness of the output (0 = deterministic, 1 = more random)
    "max_tokens": 1500,  # Maximum number of tokens to generate in the completion
    "top_p": 1,          # Nucleus sampling parameter; includes the most probable tokens whose cumulative probability exceeds this value
    "frequency_penalty": 0.0,  # Reduces the likelihood of repeating phrases (range: -2.0 to 2.0)
    "presence_penalty": 0.0,    # Reduces the likelihood of introducing new topics (range: -2.0 to 2.0)
}

MODEL_PATH = "./models/New_EnetV2_model.h5"