from pydantic_settings import SettingsConfigDict, BaseSettings
import os


class MoodMap(BaseSettings):

    RUSTIC : str
    UNIQUE : str
    GLAMOUROUS: str
    MINIMAL: str
    LUXURIOUS: str
    MODERN: str
    
    model_config = SettingsConfigDict(env_file=os.path.join(os.environ["INTERIOR_TEACHER_PROJECT"], "property/moodmap"), case_sensitive=True)
