from pydantic_settings import SettingsConfigDict, BaseSettings
import os

class BedTypeMap(BaseSettings):

    HOTEL: str
    STORAGE: str
    LOW_RAISE: str
    NORMAL: str


    model_config = SettingsConfigDict(env_file=os.path.join(os.environ["INTERIOR_TEACHER_PROJECT"], "property/type/bedtypemap"), case_sensitive=True)
