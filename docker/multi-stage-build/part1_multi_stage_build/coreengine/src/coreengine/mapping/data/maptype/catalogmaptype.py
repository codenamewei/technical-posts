from enum import Enum


class CatalogMapType(str, Enum):
    CATEGORY = "CATEGORY"
    PRICE_RANGE = "PRICE_RANGE"
    HARDNESS = "HARDNESS"
    INPUT_TAG = 'INPUT_TAG'
    OUTPUT_TAG = 'OUTPUT_TAG'
    OUTPUT_FEATURE_TAG = 'OUTPUT_FEATURE_TAG'
    PRODUCT_TAG = "PRODUCT_TAG"
    MATERIAL = "MATERIAL"
    STYLE = "STYLE"
    MOOD = "MOOD"
    BOOLEAN = "BOOLEAN"
    COLOR = "COLOR"
    SHAPE = "SHAPE"
    STORAGE_CLASS = "STORAGE_CLASS"
    LIGHTING_METHOD = "LIGHTING_METHOD"
    CHAIR_BACK_SHAPE = "CHAIR_BACK_SHAPE"
    TABLE_TOP_SHAPE = "TABLE_TOP_SHAPE"
    BED_TYPE = "BED_TYPE"
    FLOOR_LAMP_TYPE = "FLOOR_LAMP_TYPE"
    LOUNGE_CHAIR_TYPE = "LOUNGE_CHAIR_TYPE"
    PENDANT_LAMP_TYPE = "PENDANT_LAMP_TYPE"
    SOFA_TYPE = "SOFA_TYPE"
    STORAGE_DOOR_TYPE = "STORAGE_DOOR_TYPE"
    TABLE_FRAME_TYPE="TABLE_FRAME_TYPE"
    NUM_USERS="NUM_USERS"
    TYPE_OF_SPACE="TYPE_OF_SPACE"
    MAIN_ACTIVITIES="MAIN_ACTIVITIES"
    PROJECT_PROGRESS="PROJECT_PROGRESS"
    LEG_PRESENCE="LEG_PRESENCE"
    ARMREST_PRESENCE="ARMREST_PRESENCE"
    FOOTSTOOL_PRESENCE="FOOTSTOOL_PRESENCE"
    LIGHT_BULB_PRESENCE="LIGHT_BULB_PRESENCE"