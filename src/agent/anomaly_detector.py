import numpy as np

def detect_anomalies(time_series_data):
    """
    Basic Z-score based anomaly detection for AIOps metrics.
    """
    if not time_series_data:
        return []
    
    data = np.array(time_series_data)
    mean = np.mean(data)
    std = np.std(data)
    
    threshold = 3
    anomalies = []
    
    for idx, value in enumerate(data):
        z_score = (value - mean) / std if std > 0 else 0
        if abs(z_score) > threshold:
            anomalies.append({"index": idx, "value": value, "score": z_score})
            
    return anomalies
