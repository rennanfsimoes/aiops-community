"""
AIOps Community — Incident RCA & Anomaly Detection Agent
Analyzes metric spikes and correlates logs using LLM reasoning.
"""
import os
import json
import logging
from typing import Dict, Any, List

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

class AIOpsAgent:
    def __init__(self, prometheus_endpoint: str = "http://localhost:9090"):
        self.prometheus_endpoint = prometheus_endpoint
        logging.info(f"Initialized AIOps Agent connected to {self.prometheus_endpoint}")

    def evaluate_metric_series(self, metric_name: str, values: List[float], threshold_z: float = 2.5) -> Dict[str, Any]:
        """Calculates Z-Score anomaly detection on telemetry window"""
        if not values:
            return {"is_anomalous": False, "confidence": 0.0}

        avg = sum(values) / len(values)
        variance = sum((x - avg) ** 2 for x in values) / len(values)
        std_dev = (variance ** 0.5) if variance > 0 else 0.0001
        
        last_val = values[-1]
        z_score = abs(last_val - avg) / std_dev
        is_anomalous = z_score > threshold_z

        return {
            "metric": metric_name,
            "current_value": last_val,
            "baseline_avg": round(avg, 2),
            "z_score": round(z_score, 2),
            "is_anomalous": is_anomalous,
            "suggested_action": "Scale Pod replicas via HPA or investigate memory leak in container" if is_anomalous else "Normal operation"
        }

if __name__ == "__main__":
    agent = AIOpsAgent()
    sample_metrics = [42.1, 44.0, 43.5, 45.2, 42.8, 98.6]
    result = agent.evaluate_metric_series("container_memory_usage_bytes", sample_metrics)
    print(json.dumps(result, indent=2))
