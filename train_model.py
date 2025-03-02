import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

# Load and preprocess data
df = pd.read_csv('network_traffic.csv')
df = pd.get_dummies(df, columns=['protocol', 'src_ip', 'dest_ip'])  # Ensure 'dest_ip' matches the column name in the dataset
X = df.drop(columns=['src_port', 'dest_port'])

# Train model
model = IsolationForest(contamination=0.01)
model.fit(X)

# Save model
joblib.dump(model, 'model.pkl')
