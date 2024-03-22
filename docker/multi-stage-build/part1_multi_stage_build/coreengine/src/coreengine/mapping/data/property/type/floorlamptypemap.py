from pydantic_settings import SettingsConfigDict, BaseSettings
import os

class FloorLampTypeMap(BaseSettings):

    ATYPICAL: str
    STRAIGHT: str
    MULTI_HEAD: str
    JOINT: str
    LONG: str
    
    model_config = SettingsConfigDict(env_file=os.path.join(os.environ["INTERIOR_TEACHER_PROJECT"], "property/type/floorlamptypemap"), case_sensitive=True)
