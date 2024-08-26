from huggingface_hub import InferenceClient
import json
from config import Settings

# * Testing using the Inference Client for HF repos that have serverless inferences available


# Hugging Face Inference Client Setup

# Repository ID for the model to be used
repo_id = "microsoft/Phi-3-mini-4k-instruct"
# Load settings from the config file
settings = Settings()

# Initialize the Inference Client
llm_client = InferenceClient(
    model=repo_id,
    timeout=120,
    token=settings.hf_api_testing
)


def call_llm(inference_client: InferenceClient, prompt: str) -> str:
    """
    Send a prompt to the language model and get the generated response.

    Args:
        inference_client (InferenceClient): The initialized Hugging Face Inference Client.
        prompt (str): The input prompt for the language model.

    Returns:
        str: The generated text response from the model.
    """
    response = inference_client.post(
        json={
            "inputs": prompt,
            "parameters": {"max_new_tokens": 200},

        }
    )
    return json.loads(response.decode())[0]["generated_text"]


response = call_llm(llm_client, "How are you?")
print(response)
