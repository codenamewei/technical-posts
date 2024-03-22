from pydantic_settings import SettingsConfigDict, BaseSettings
import os

class FurnitureMap(BaseSettings):

    # CHAIR
    SOFA : str
    CHAIR : str
    LOUNGE_CHAIR : str
    OFFICE_CHAIR: str
    STOOL_BENCH : str
    
    # TABLE
    COFFEE_TABLE: str
    SIDE_TABLE: str
    DINING_TABLE: str
    TABLE: str
    DESK: str

    # storage
    STORAGE: str
    BOOK_SHELF: str

    # lamp
    FLOOR_LAMP : str
    TABLE_LAMP : str
    PENDANT_LAMP : str


    # other
    BED: str

    model_config = SettingsConfigDict(env_file=os.path.join(os.environ["INTERIOR_TEACHER_PROJECT"], "header/furniture_map"), case_sensitive=True)
