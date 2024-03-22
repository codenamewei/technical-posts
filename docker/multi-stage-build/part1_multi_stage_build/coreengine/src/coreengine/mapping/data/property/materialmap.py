from pydantic_settings import SettingsConfigDict, BaseSettings
import os

class MaterialMap(BaseSettings):

    HARDWOOD: str

    PROCESSED_WOOD: str
    PROCESSED_WOOD_LAMINATED: str
    GLASS : str

    MARBLE: str
    CERAMIC: str
    PLASTIC: str

    STEEL_METAL: str
    LEATHER: str
    VELVET: str

    FABRIC: str
    ACRYLIC: str
    SUEDE: str

    WOOD: str
    FUNCTIONAL_FABRIC: str
    STONE: str

    PAPER: str
    VELVET_SUEDE: str
    POTTERY: str

    MESH : str
    RATTAN : str

    model_config = SettingsConfigDict(env_file=os.path.join(os.environ["INTERIOR_TEACHER_PROJECT"], "property/materialmap"), case_sensitive=True)
