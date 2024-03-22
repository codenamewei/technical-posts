from pydantic_settings import SettingsConfigDict, BaseSettings
import os


class ProjectProgressMap(BaseSettings):

    COMPLETE : str
    TERMINATED : str
    FURNITURE_PURCHASE: str
    FURNITURE_PURCHASE_IN_PROGRESS: str
    DESIGN_IN_PROGRESS: str
    
    model_config = SettingsConfigDict(env_file=os.path.join(os.environ["INTERIOR_TEACHER_PROJECT"], "property/projectprogressmap"), case_sensitive=True)
