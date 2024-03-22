from pydantic_settings import SettingsConfigDict, BaseSettings
import os


class LightingMethodMap(BaseSettings):

    DIRECT : str
    INDIRECT : str
    
    model_config = SettingsConfigDict(env_file=os.path.join(os.environ["INTERIOR_TEACHER_PROJECT"], "property/lightingmethodmap"), case_sensitive=True)
