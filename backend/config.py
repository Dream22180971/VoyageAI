from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    deepseek_api_key: str
    openweather_api_key: str
    amap_api_key: str
    database_url: str = "sqlite:///./voyageai.db"
    cache_timeout: int = 300
    
    class Config:
        env_file = ".env"

settings = Settings()
