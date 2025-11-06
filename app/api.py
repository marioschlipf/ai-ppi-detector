from fastapi import APIRouter, Depends, UploadFile, File
from .models import PIIDetectionRequest, PIIDetectionResponse, FileContentResponse
from .services import pii_service, PIIService
from .file_processing import file_processing_service, FileProcessingService

router = APIRouter()

@router.post(
    "/detect-pii",
    response_model=PIIDetectionResponse,
    summary="Detect PII in Text",
    description="Analyzes a string of text and returns any detected Personally Identifiable Information (PII).",
    tags=["PII Detection"],
)
async def detect_pii(
    request: PIIDetectionRequest,
    service: PIIService = Depends(lambda: pii_service),
):
    detections = service.detect_pii(request.text)
    return PIIDetectionResponse(detections=detections)


@router.post(
    "/extract-text",
    response_model=FileContentResponse,
    summary="Extract Text from a File",
    description="Upload a file to extract its text content. The extracted text is returned as a string.",
    tags=["File Processing"],
)
async def extract_text(
    file: UploadFile = File(..., description="The file to process."),
    file_processing_service_instance: FileProcessingService = Depends(
        lambda: file_processing_service
    ),
):
    text = file_processing_service_instance.extract_text_from_file(file)
    return FileContentResponse(text=text)
