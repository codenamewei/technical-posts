from pydantic_settings import SettingsConfigDict, BaseSettings
import os

class StorageDoorTypeMap(BaseSettings):

    NONE: str
    HINGED: str
    SLIDING: str
    FLAP: str
    model_config = SettingsConfigDict(env_file=os.path.join(os.environ["INTERIOR_TEACHER_PROJECT"], "property/type/storagedoortypemap"), case_sensitive=True)