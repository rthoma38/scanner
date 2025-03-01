import joblib
import pyshark
import pandas as pd

# Load model
model = joblib.load('model.pkl')

def detect_anomalies(model):
    cap = pyshark.LiveCapture(interface='eth0')
    for packet in cap.sniff_continuously():
        try:
            features = {
                'length': int(packet.length),
                'protocol': packet.transport_layer,
                'src_ip': packet.ip.src,
                'dst_ip': packet.ip.dst,
                'src_port': packet[packet.transport_layer].srcport,
                'dst_port': packet[packet.transport_layer].dstport,
            }
            df = pd.DataFrame([features])
            df = pd.get_dummies(df, columns=['protocol', 'src_ip', 'dst_ip'])
            prediction = model.predict(df)
            if prediction == -1:
                print(f"Anomaly detected: {features}")
        except AttributeError:
            continue

detect_anomalies(model)
