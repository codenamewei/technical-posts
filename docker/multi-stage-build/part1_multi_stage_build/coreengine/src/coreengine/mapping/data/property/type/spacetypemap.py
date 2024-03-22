from pydantic_settings import SettingsConfigDict, BaseSettings
import os

class SpaceTypeMap(BaseSettings):

    LIVING_ROOM: str
    BALCONY : str
    PARTY_ROOM: str
    
    RESIDENTIAL_SPACE: str
    STUDIO: str
    PREMIUM_RESIDENTIAL_SPACE: str

    COMMERCIAL_SPACE: str
    ONE_ROOM: str
    OFFICE: str

    BEDROOM: str
    DINING: str
    KITCHEN: str
    
    STUDY_ROOM: str
    DRESSING_ROOM: str
    GUEST_ROOM: str

    ALPHA_ROOM: str
    ATTIC: str
    HOBBY: str

    LOUNGE_BAR: str



    model_config = SettingsConfigDict(env_file=os.path.join(os.environ["INTERIOR_TEACHER_PROJECT"], "property/type/spacetypemap"), case_sensitive=True)
