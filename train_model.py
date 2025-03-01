import pandas as pd
from sklearn.ensemble import IsolationForest

# Load and preprocess data
df = pd.read_csv('network_traffic.csv')
df = pd.get_dummies(df, columns=['protocol', 'src_ip', 'dst_ip'])
X = df.drop(columns=['src_port', 'dst_port'])

# Train model
model = IsolationForest(contamination=0.01)
model.fit(X)

# Save model
import joblib
joblib.dump(model, 'model.pkl')
