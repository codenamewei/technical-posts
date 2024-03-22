from pydantic_settings import SettingsConfigDict, BaseSettings
import os

class PendantLampTypeMap(BaseSettings):

    MULTI_HEAD: str
    NORMAL: str
    LINE: str

    model_config = SettingsConfigDict(env_file=os.path.join(os.environ["INTERIOR_TEACHER_PROJECT"], "property/type/pendantlamptypemap"), case_sensitive=True)
