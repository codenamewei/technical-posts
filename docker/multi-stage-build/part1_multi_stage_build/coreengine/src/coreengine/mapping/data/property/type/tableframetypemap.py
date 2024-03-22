from pydantic_settings import SettingsConfigDict, BaseSettings
import os

class TableFrameTypeMap(BaseSettings):

    OPEN: str
    CLOSE: str
    model_config = SettingsConfigDict(env_file=os.path.join(os.environ["INTERIOR_TEACHER_PROJECT"], "property/type/tableframetypemap"), case_sensitive=True)
