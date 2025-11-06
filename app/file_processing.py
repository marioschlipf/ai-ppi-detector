import magic
from fastapi import UploadFile
from unstructured.partition.auto import partition

class FileProcessingService:
    def __init__(self):
        pass

    def extract_text_from_file(self, file: UploadFile) -> str:
        mime_type = magic.from_buffer(file.file.read(2048), mime=True)
        file.file.seek(0)

        if mime_type == "application/pdf":
            elements = partition(file=file.file, content_type=mime_type)
            return "\n\n".join([str(el) for el in elements])
        elif mime_type == "text/plain":
            return file.file.read().decode("utf-8")
        else:
            raise ValueError(f"Unsupported file type: {mime_type}")

file_processing_service = FileProcessingService()

