from pydantic import BaseModel

class PredictionItem(BaseModel):
    product_id : int
    product_name : str
    category: str
    price: int = 0
    url : str
    prediction_score: float | None = None