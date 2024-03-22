from pydantic import BaseModel

class PredictionInput(BaseModel):

    space : str 
    styles_in_str : str#list[str]
    activities_in_str : str#list[str]

    budget_min: int
    budget_max: int

    design_request: str