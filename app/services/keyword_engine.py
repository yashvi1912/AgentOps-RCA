from typing import Dict, List


class KeywordEngine:
    """
    Rule-based keyword matching engine.
    """

    def predict(self, message: str, incidents: List[Dict]) -> Dict:

        message = message.lower()

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
                "predicted_root_cause": best_match["root_cause"],
                "severity": best_match["severity"],
                "confidence": round(min(best_score / 5, 1.0), 2)
            }

        return {
            "predicted_root_cause": "unknown",
            "severity": "unknown",
            "confidence": 0
        }


keyword_engine = KeywordEngine()