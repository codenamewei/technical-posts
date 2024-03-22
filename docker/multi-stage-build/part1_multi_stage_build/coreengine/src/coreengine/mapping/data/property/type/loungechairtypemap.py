from pydantic_settings import SettingsConfigDict, BaseSettings
import os

class LoungeChairTypeMap(BaseSettings):

    LOUNGE_CHAIR: str
    LOUNGE_SOFA: str

    model_config = SettingsConfigDict(env_file=os.path.join(os.environ["INTERIOR_TEACHER_PROJECT"], "property/type/loungechairtypemap"), case_sensitive=True)
