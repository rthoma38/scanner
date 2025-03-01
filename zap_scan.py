import os
import time
from zapv2 import ZAPv2

api_key = os.getenv('ZAP_API_KEY')  # Get the API key from the environment variable
zap = ZAPv2(apikey=api_key, proxies={'http': 'http://127.0.0.1:8081', 'https': 'http://127.0.0.1:8081'})

print("Ensuring ZAP is ready...")
time.sleep(10)

print("Starting a new session...")
zap.core.new_session(name='new_session', overwrite=True)

target = 'http://127.0.0.1:5000'  # Replace with your actual target URL
print(f'Starting scan on target {target}')
zap.urlopen(target)  # Access the target URL
scan_id = zap.ascan.scan(target)

while int(zap.ascan.status(scan_id)) < 100:
    print(f'Scan progress: {zap.ascan.status(scan_id)}%')
    time.sleep(5)

print('Scan completed')

report = zap.core.htmlreport()
print(f'Report length: {len(report)}')

with open('zap_report.html', 'w') as report_file:
    report_file.write(report)
print('Report generated: zap_report.html')
