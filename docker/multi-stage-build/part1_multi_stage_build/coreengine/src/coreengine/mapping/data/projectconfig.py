from pydantic_settings import BaseSettings, SettingsConfigDict
import os

class ProjectConfig(BaseSettings):

    PROJECT_DATA_PATH : str
    MODEL_PATH : str
    LOOKUP_PATH: str
    FURNITURE_MAPPING_FILE: str
    DATA_FOLDER: str
    RAN_PREDICTION_FOLDER: str
    SAVED_PREDICTION_FOLDER : str

    #PREDICTION 
    TOP_N : int
    CONFIDENCE_THRESHOLD : float
    INCLUDE_RANDOM : bool

    # if factor price and not include_random, there is a possibility not the highest score will be selected if exceed price
    FACTOR_PRICE : bool 

    #number of units retrieved by category
    UNIT_PER_CATEGORY: int

    #temporary for training debugging
    GROUNDTRUTH_FURNITURE_PER_PROJECT : str | None = None
    
    model_config = SettingsConfigDict(env_file=os.path.join(os.environ["INTERIOR_TEACHER_PROJECT"], "projectconfig"), case_sensitive=True)