from pydantic_settings import BaseSettings

# Settings Configuration


class Settings(BaseSettings):
    """
    Configuration settings for the application.

    This class uses pydantic_settings to manage environment variables
    and configuration settings.
    """
    # Hugging Face API token for testing purposes
    hf_api_testing: str

    class Config:
        """
        Configuration for the Settings class.
        """
        # Specifies the .env file to load environment variables from
        env_file = ".env"


# Usage:
# 1. Create a .env file in the same directory as this script
# 2. Add your Hugging Face API token to the .env file:
#    HF_API_TESTING=your_api_token_here
# 3. Instantiate the Settings class:
#    settings = Settings()
# 4. Access the API token:
#    api_token = settings.hf_api_testing
