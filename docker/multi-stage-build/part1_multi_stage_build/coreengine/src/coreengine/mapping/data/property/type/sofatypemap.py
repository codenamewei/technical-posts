from pydantic_settings import SettingsConfigDict, BaseSettings
import os

class SofaTypeMap(BaseSettings):

    MODULE: str
    STRAIGHT: str
    COUCH_CORNER: str
    SEATED: str
    DAYBED_BENCH: str

    model_config = SettingsConfigDict(env_file=os.path.join(os.environ["INTERIOR_TEACHER_PROJECT"], "property/type/sofatypemap"), case_sensitive=True)
