from app.services.dataset_loader import dataset_loader
from app.services.keyword_engine import keyword_engine


class AnalysisService:
    """
    Main orchestration layer.

    Responsible for coordinating all analysis engines.
    """

    def analyze(self, message: str):

        incidents = dataset_loader.load()

        result = keyword_engine.predict(
            message=message,
            incidents=incidents
        )

        return result


analysis_service = AnalysisService()