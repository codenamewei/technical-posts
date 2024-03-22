from pydantic_settings import SettingsConfigDict, BaseSettings
import os

class TableTopShapeMap(BaseSettings):

    ATYPICAL: str
    CIRCULAR: str
    ELLIPTICAL: str
    RECTANGULAR:str
    
    model_config = SettingsConfigDict(env_file=os.path.join(os.environ["INTERIOR_TEACHER_PROJECT"], "property/tabletopshapemap"), case_sensitive=True)
