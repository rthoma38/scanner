import joblib
import pandas as pd

# Load the model
model = joblib.load('anomaly_detection_model.pkl')

def detect_anomalies(new_data):
    # Predict anomalies
    predictions = model.predict(new_data)
    return predictions

# Example usage
new_data = pd.read_csv('new_network_activity.csv')
anomalies = detect_anomalies(new_data)
print(anomalies)
