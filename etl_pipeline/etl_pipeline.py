import pandas as pd

# Load the simulated SIEM events data
df = pd.read_csv('../data_generator/simulated_siem_events.csv')

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

eventsPerSourceIP = df.groupby('source_ip').size().sort_values(ascending=False)
averageSeverity = round(df.groupby('destination_ip')['severity_score'].mean().sort_values(ascending=False), 2)
eventTypeCounts = df['event_type'].value_counts()

# Reset index after cleaning
df = df.reset_index(drop=True)

# Display the cleaned and transformed DataFrame
print('\n' + df.to_string())
print('\n' + eventsPerSourceIP[:5].to_string())
print('\n' + averageSeverity[:5].to_string())
print('\n' + eventTypeCounts.to_string())