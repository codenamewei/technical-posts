from pydantic_settings import SettingsConfigDict, BaseSettings
import os

class ColorMap(BaseSettings):

    COLORFUL: str
    MONOTONE: str
    BROWNTONE : str
    
    ACHROMATIC: str
    
    model_config = SettingsConfigDict(env_file=os.path.join(os.environ["INTERIOR_TEACHER_PROJECT"], "property/colormap"), case_sensitive=True)
