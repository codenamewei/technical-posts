from pydantic_settings import SettingsConfigDict, BaseSettings
import os

"""
Output tag contains columns that will generated from the engine recommendation 
"""

class OutputFeatureTagMap(BaseSettings):

    # CHAIR
    PRICE_RANGE : str
    HARDNESS : str
    FUNCTION : str

    LEG_PRESENCE : str
    MODELING_PRESENCE : str
    MOOD: str

    COLOR: str
    MATERIAL : str
    STYLE: str
    
    TYPE: str
    SHAPE: str
    TABLE_TOP_MATERIAL: str
    
    LOUNGE_CHAIR_SEAT_MATERIAL : str

    SOFA_TYPE : str
    LOUNGE_CHAIR_TYPE : str
    BED_TYPE: str

    FLOOR_LAMP_TYPE: str
    PENDANT_LAMP_TYPE: str

    TABLE_TOP_SHAPE: str
    TABLE_FRAME_TYPE : str
    TABLE_LEG_MATERIAL: str    

    CHAIR_BACK_MATERIAL: str
    CHAIR_BACK_SHAPE : str
    CHAIR_SEAT_MATERIAL : str

    ARMREST_PRESENCE: str
    FOOTSTOOL_PRESENCE: str

    FRAME_MATERIAL : str
    NUM_USERS : str

    STORAGE_CLASS : str
    STORAGE_DOOR_TYPE : str
    LIGHT_BULB_PRESENCE: str

    LIGHTING_METHOD: str
    HEAD_MATERIAL: str

    model_config = SettingsConfigDict(env_file=os.path.join(os.environ["INTERIOR_TEACHER_PROJECT"], "header/output_feature_tag"), case_sensitive=True)
