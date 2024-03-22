from pydantic_settings import SettingsConfigDict, BaseSettings
import os

"""
Output tag contains columns that will generated from the engine recommendation 
"""

class InputTagMap(BaseSettings):

    PROJECT_ID : str
    COUNSELING_ID : str
    PROJECT_PROGRESS : str
    SPACE_AREA : str
    SPACE : str
    DESIGNER1 : str
    DESIGNER2 : str
    BUDGET: str
    COMPLEXITY: str
    TYPE_OF_SPACE: str
    STYLE: str
    URL: str
    MAIN_ACTIVITIES: str
    DESIGN_REQUEST : str
    INTERNAL_MEMO: str

    model_config = SettingsConfigDict(env_file=os.path.join(os.environ["INTERIOR_TEACHER_PROJECT"], "header/input_tag"), case_sensitive=True)
