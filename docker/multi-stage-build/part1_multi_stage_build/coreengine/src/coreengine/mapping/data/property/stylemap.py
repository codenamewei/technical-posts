from pydantic_settings import SettingsConfigDict, BaseSettings
import os

"""
Output tag contains columns that will generated from the engine recommendation 
"""

class StyleMap(BaseSettings):

    MODERN: str
    NATURAL_BEIGE: str
    MIDCENTURY_POP : str

    VINTAGE : str
    NORTH_EUROPE: str
    ORIENTAL : str

    ETHNIC : str
    KIDULT : str
    FRENCH_MODERN: str
    
    UNIQUE : str
    NATURAL_DARK_BROWN : str
    MIDCENTURY_VINTAGE : str

    MIDCENTURY_MODERN : str
    NORTH_EUROPE_PATTERN : str
    CLASSIC : str

    LUXURY : str
    KIDS: str
    FRENCH : str
    
    NATURAL : str
    
    
    model_config = SettingsConfigDict(env_file=os.path.join(os.environ["INTERIOR_TEACHER_PROJECT"], "property/stylemap"), case_sensitive=True)
