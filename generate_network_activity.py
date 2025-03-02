import pandas as pd
import numpy as np

# Set the random seed for reproducibility
np.random.seed(42)

# Define the number of samples
num_samples = 1000

# Generate synthetic features
src_ip = np.random.choice(['192.168.1.1', '192.168.1.2', '192.168.1.3'], num_samples)
dest_ip = np.random.choice(['10.0.0.1', '10.0.0.2', '10.0.0.3'], num_samples)
src_port = np.random.randint(1024, 65535, num_samples)
dest_port = np.random.randint(1024, 65535, num_samples)
protocol = np.random.choice(['TCP', 'UDP'], num_samples)
packet_size = np.random.randint(64, 1500, num_samples)
duration = np.random.uniform(0.1, 10.0, num_samples)

# Generate synthetic labels (0 for normal, 1 for anomaly)
labels = np.random.choice([0, 1], num_samples, p=[0.95, 0.05])

# Create a DataFrame
data = pd.DataFrame({
    'src_ip': src_ip,
    'dest_ip': dest_ip,
    'src_port': src_port,
    'dest_port': dest_port,
    'protocol': protocol,
    'packet_size': packet_size,
    'duration': duration,
    'label': labels
})

# Save the DataFrame to a CSV file
data.to_csv('network_traffic.csv', index=False)
