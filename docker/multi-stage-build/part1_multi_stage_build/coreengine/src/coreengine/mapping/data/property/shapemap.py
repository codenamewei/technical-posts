from pydantic_settings import SettingsConfigDict, BaseSettings
import os

class ShapeMap(BaseSettings):

    ATYPICAL: str
    STRAIGHT: str
    CURVE: str
    STONE:str
    
    model_config = SettingsConfigDict(env_file=os.path.join(os.environ["INTERIOR_TEACHER_PROJECT"], "property/shapemap"), case_sensitive=True)
