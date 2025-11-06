from fastapi import APIRouter, Depends
from .models import PIIDetectionRequest, PIIDetectionResponse
from .services import pii_service, PIIService

router = APIRouter()

@router.post("/detect-pii", response_model=PIIDetectionResponse)
async def detect_pii(
    request: PIIDetectionRequest,
    service: PIIService = Depends(lambda: pii_service)
):
    detections = service.detect_pii(request.text)
    return PIIDetectionResponse(detections=detections)

