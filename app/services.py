from gliner import GLiNER

from .models import PIIDetection


class PIIService:
    def __init__(self):
        # Initialize and load the GLiNER model
        self.model = GLiNER.from_pretrained("knowledgator/gliner-pii-large-v1.0")

    def detect_pii(self, text: str) -> list[PIIDetection]:
        # Define the PII labels you want to detect
        labels = [
            "name", "dob", "discharge date", "organization medical facility",
            "email address", "phone number", "policy number"
        ]
        # Perform PII detection
        entities = self.model.predict_entities(text, labels)

        # Format the detections
        detections = []
        for entity in entities:
            detections.append(
                PIIDetection(
                    text=entity["text"],
                    start=entity["start"],
                    end=entity["end"],
                    label=entity["label"],
                    score=entity["score"]
                )
            )
        return detections


pii_service = PIIService()
