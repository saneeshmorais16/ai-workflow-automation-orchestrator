from pydantic import BaseModel,Field
from typing import Literal
class WorkflowCreate(BaseModel):
    title:str=Field(min_length=3);request_description:str=Field(min_length=8);requester:str="Synthetic Requester";business_area:str="General Operations";priority:Literal["low","medium","high"]="medium"
class ReviewRequest(BaseModel):reviewer_note:str=Field(min_length=1)
