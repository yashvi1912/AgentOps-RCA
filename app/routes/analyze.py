import json
from pathlib import Path

from fastapi import APIRouter

router = APIRouter(
    prefix="/analyze",
    tags=["Analysis"]
)

DATASET_PATH = Path("datasets/incidents.json")


@router.post("/")
def analyze_log(payload: dict):

    message = payload.get("message", "").lower()

    with open(DATASET_PATH, "r") as f:
        incidents = json.load(f)

    best_match = None
    best_score = 0

    for incident in incidents:

        score = 0

        for log in incident["logs"]:

            log = log.lower()

            for word in message.split():
                if word in log:
                    score += 1

        if score > best_score:
            best_score = score
            best_match = incident

    if best_match:

        return {
            "predicted_root_cause":
                best_match["root_cause"],
            "severity":
                best_match["severity"],
            "confidence":
                round(min(best_score / 5, 1.0), 2)
        }

    return {
        "predicted_root_cause":
            "unknown",
        "confidence":
            0
    }