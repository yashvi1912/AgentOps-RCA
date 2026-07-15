import json
from pathlib import Path
from typing import List, Dict


class DatasetLoader:
    """
    Loads and caches the incident dataset.

    The dataset is loaded only once when the application starts.
    """

    def __init__(self):
        self.dataset_path = Path("datasets/incidents.json")
        self._incidents = None

    def load(self) -> List[Dict]:
        """Load dataset into memory."""

        if self._incidents is None:
            with open(self.dataset_path, "r", encoding="utf-8") as file:
                self._incidents = json.load(file)

        return self._incidents

    def reload(self):
        """Force reload dataset."""

        self._incidents = None
        return self.load()


dataset_loader = DatasetLoader()