from pydantic_settings import SettingsConfigDict, BaseSettings
import os

"""
Output tag contains columns that will generated from the engine recommendation 
"""

class OutputTagMap(BaseSettings):

    PROJECT_ID : str
    SPACE : str
    PRODUCT_NAME : str

    ID : str
    CATEGORY : str
    UNIT: str

    model_config = SettingsConfigDict(env_file=os.path.join(os.environ["INTERIOR_TEACHER_PROJECT"], "header/output_tag"), case_sensitive=True)
