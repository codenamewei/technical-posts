from pydantic import BaseModel

class GroundTruthItem(BaseModel):
    product_id : int
    product_name : str
    category: str
    unit : int