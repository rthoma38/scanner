import pandas as pd

# Load the training data
training_data = pd.read_csv('/var/lib/jenkins/workspace/midterm/network_traffic.csv')

# Load the new data
new_data = pd.read_csv('/var/lib/jenkins/workspace/midterm/network_traffic.csv')

# Get the feature names from both datasets
training_features = set(training_data.columns)
new_data_features = set(new_data.columns)

# Find differences
missing_in_new_data = training_features - new_data_features
extra_in_new_data = new_data_features - training_features

print("Missing in new data:", missing_in_new_data)
print("Extra in new data:", extra_in_new_data)

# Rename columns in new data to match training data if necessary
# Assuming that the columns need to be renamed based on the differences found
rename_mapping = {
    'dest_ip': 'dest_ip_10.0.0.1',  # Example mapping, update based on actual differences
    'protocol': 'protocol_TCP',     # Example mapping, update based on actual differences
    # Add more renaming mappings as needed
}

new_data.rename(columns=rename_mapping, inplace=True)

# Save the updated new data to a new CSV file
new_data.to_csv('/var/lib/jenkins/workspace/midterm/updated_network_traffic.csv', index=False)

print("New data columns after renaming:", new_data.columns)
