from .outputfeaturetagmap import OutputFeatureTagMap
from pydantic_settings import SettingsConfigDict
import os

"""
Output tag contains columns that will generated from the engine recommendation 
"""

class ProductTagMap(OutputFeatureTagMap):

    PRODUCT_NAME : str
    ID : str
    CATEGORY : str

    URL : str
    PRICE: str
    SHIPPING: str

    NUM_USERS: str
    SIZE: str
    OHOUSE: str


    model_config = SettingsConfigDict(env_file=os.path.join(os.environ["INTERIOR_TEACHER_PROJECT"], "header/product_tag"), case_sensitive=True)
