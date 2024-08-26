# HuggingFace Inference API Testing

This project provides a simple setup for testing HuggingFace Inference APIs from local Python applications.
It includes configuration management and a client for making inference requests to HuggingFace models.

## Features

- Configuration management using Pydantic BaseSettings
- Hugging Face Inference Client setup
- Example usage of the Inference API

## Setup and Usage

Create a `.env` file in the project root and add your HuggingFace API token:
`HF_API_TESTING=your_api_token_here`

The project consists of two main files:

### `config.py`

This file sets up the configuration using Pydantic BaseSettings

### `inference_client.py`

This file sets up the HuggingFace Inference Client and provides a function to call the language model

## Example Projects

[VITON-HD Repository](https://github.com/shadow2496/VITON-HD)

[IDM-VTON on HuggingFace](https://huggingface.co/yisol/IDM-VTON)

[Gradio Test UI](https://huggingface.co/spaces/yisol/IDM-VTON)
