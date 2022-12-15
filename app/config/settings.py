from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    title: str = "FastAPI Basic Template"
    version: str = "0.0.1"
    debug: bool = False

    api_prefix_v1: str = "/api/v1"
    api_docs: str = "/docs/"
    api_openapi: str = "/openapi.json"


@lru_cache()
def get_settings() -> Settings:
    return Settings()
