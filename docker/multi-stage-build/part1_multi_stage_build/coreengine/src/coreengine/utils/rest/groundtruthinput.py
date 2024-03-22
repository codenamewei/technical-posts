from pydantic import BaseModel

class GroundTruthInput(BaseModel):

    project_id : int
    space_id : int