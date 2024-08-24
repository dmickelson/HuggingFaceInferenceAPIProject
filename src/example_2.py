# Testing using https://huggingface.co/yisol/IDM-VTON

from huggingface_hub import InferenceClient
import json
from config import Settings

repo_id = "microsoft/Phi-3-mini-4k-instruct"
settings = Settings()

llm_client = InferenceClient(
    model=repo_id,
    timeout=120,
    token=settings.hf_api_testing
)


def call_llm(inference_client: InferenceClient, prompt: str) -> str:
    response = inference_client.post(
        json={
            "inputs": prompt,
            "parameters": {"max_new_tokens": 200},

        }
    )
    return json.loads(response.decode())[0]["generated_text"]


response = call_llm(llm_client, "How are you?")
print(response)
