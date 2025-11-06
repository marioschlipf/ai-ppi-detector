from pydantic import BaseModel
from typing import List

class PIIDetectionRequest(BaseModel):
    text: str

class PIIDetection(BaseModel):
    text: str
    start: int
    end: int
    label: str
    score: float

class PIIDetectionResponse(BaseModel):
    detections: List[PIIDetection]

