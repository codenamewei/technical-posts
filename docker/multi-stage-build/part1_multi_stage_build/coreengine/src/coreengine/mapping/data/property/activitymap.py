from pydantic_settings import SettingsConfigDict, BaseSettings
import os

class ActivityMap(BaseSettings):

    STORAGE : str
    WORK : str
    GAME : str

    HOME_TRAINING : str
    PET : str
    REST : str

    STUDY : str
    MUSIC : str
    INSTRUMENT_PLAY : str

    ART : str
    MOVIE : str
    TV : str

    COOKING : str
    WINE : str
    GUEST_WELCOME : str

    TEA_CEREMONY : str
    MEAL :str
    
    model_config = SettingsConfigDict(env_file=os.path.join(os.environ["INTERIOR_TEACHER_PROJECT"], "property/activitymap"), case_sensitive=True)
