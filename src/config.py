from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    hf_api_testing: str

    class Config:
        env_file = ".env"
