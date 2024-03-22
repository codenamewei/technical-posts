from pydantic_settings import SettingsConfigDict, BaseSettings
import os

class ChairBackShapeMap(BaseSettings):

    STOOL: str
    COMPLETELY_BLOCKED: str
    PARTIALLY_BLOCKED: str


    model_config = SettingsConfigDict(env_file=os.path.join(os.environ["INTERIOR_TEACHER_PROJECT"], "property/chairbackshapemap"), case_sensitive=True)
