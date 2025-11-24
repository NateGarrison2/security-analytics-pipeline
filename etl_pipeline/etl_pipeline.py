import pandas as pd
import os

# Dynamically determine the data folder path relative to this script
data_dir = os.path.join(os.path.dirname(__file__), 'data')
os.makedirs(data_dir, exist_ok=True)

# Load the simulated SIEM events data
input_file = os.path.join(data_dir, 'simulated_siem_events.csv')
df = pd.read_csv(input_file)

# Normalize column names, convert timestamp to datetime, and sort by timestamp
df.columns = df.columns.str.lower().str.replace(' ', '_')
df['timestamp'] = pd.to_datetime(df['timestamp'])
df = df.sort_values(by='timestamp')

# Data cleaning: Remove rows with critical missing values based on event_type
df = df.dropna(subset=['timestamp', 'event_type'])

# Map event types to severity levels
severityMap = {
    "login_success": 'low',
    "login_failure": 'medium',
    "multiple_login_failures": 'medium',
    "firewall_block": 'medium',
    "malware_detected": 'high',
    "data_exfiltration": 'critical',
    "privilege_escalation": 'high',
    "ddos_attack": 'high',
    "ransomware_activity": 'critical'
}

severityNumMap = {
    'low': 1,
    'medium': 2,
    'high': 3,
    'critical': 4
}

# Create new columns for severity and severity score
df['severity'] = df['event_type'].map(severityMap)
df['severity_score'] = df['severity'].map(severityNumMap)

# Data transformation: Aggregate data to find counts and average severity per source IP
eventsPerSourceIP = df.groupby('source_ip').size().sort_values(ascending=False)
averageSeverity = round(df.groupby('destination_ip')['severity_score'].mean().sort_values(ascending=False), 2)
eventTypeCounts = df['event_type'].value_counts()

# Reset index after cleaning
df = df.reset_index(drop=True)

# Save the cleaned and transformed data to a new CSV file dynamically
output_file = os.path.join(data_dir, 'cleaned_siem_events.csv')
df.to_csv(output_file, index=False)

# Display the cleaned and transformed DataFrame
print('\n' + f"{df}")
print('\nHighest event counts per source IP:\n' + eventsPerSourceIP[:5].to_string())
print('\nHighest average severity per destination IP:\n' + averageSeverity[:5].to_string())
print('\nCounts of event type:\n' + eventTypeCounts.to_string())
print(f'\nCleaned data saved to {output_file}')
