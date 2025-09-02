# Import libraries
import datetime
from datetime import datetime, timedelta
from math import e
import random
import pandas as pd

# Function to generate random time between start date/time and end date/time
def generateRandomDateTime(start, end):
    timeDelta = end - start
    randomSeconds = random.uniform(0, timeDelta.total_seconds())
    # Have a 1% chance of returning None to simulate null values
    if random.random() < 0.99:
        return (start + timedelta(seconds=randomSeconds)).strftime("%Y-%m-%d %H:%M:%S")
    else:
        return None

# Function to generate random SIEM event type
def generateRandomEventType():
    eventTypes = [
        "login_success",
        "login_failure",
        "multiple_login_failures",
        "firewall_block",
        "malware_detected",
        "data_exfiltration",
        "privilege_escalation",
        "ddos_attack",
        "ransomware_activity"
    ]
    weights = [
        0.55,  # login_success 
        0.18,  # login_failure 
        0.05,  # multiple_login_failures 
        0.09,  # firewall_block 
        0.05,  # malware_detected 
        0.02,  # data_exfiltration 
        0.02,  # privilege_escalation 
        0.005, # ddos_attack 
        0.005  # ransomware_activity 
    ]
    # Have a 1% chance of returning None to simulate null values
    if random.random() < 0.99:
        return random.choices(eventTypes, weights)[0]
    else:
        return None

# Function to generate a full event log entry
def generateEvent():
    eventDateTime = generateRandomDateTime(startDateTime, currentDateTime)
    sourceIP = random.choice(sourceAddressList)
    destIP = random.choice(destAddressList)
    eventType = generateRandomEventType()
    data.append([eventDateTime, sourceIP, destIP, eventType])
  
sourceAddressList = []
for i in range (80):
    octets = []
    for j in range (4):
        if j == 0:
            # Ensure first octet is between 1 and 223 (excluding private/reserved ranges)
            firstOctet = random.randint(1, 223)
            if firstOctet == 10 or (firstOctet == 172) or (firstOctet == 192):
                firstOctet += 1
            octets.append(str(firstOctet))
        else:
            octets.append(str(random.randint(0, 255)))
        ipAddress = ".".join(octets)
    # Have a 1% chance of excluding the IP address to simulate null values
    if random.random() < 0.99:
        sourceAddressList.append(ipAddress)
    else:
        sourceAddressList.append(None)
    

destAddressList = []
for i in range (50):
    octets = []
    for j in range (4):
        if j == 0:
            # Ensure first octet is 10 (private range Class A)
            firstOctet = 10
            octets.append(str(firstOctet))
        else:
            octets.append(str(random.randint(0, 255)))
        ipAddress = ".".join(octets)
    # Have a 1% chance of excluding the IP address to simulate null values
    if random.random() < 0.99:
        destAddressList.append(ipAddress)
    else:
        destAddressList.append(None)

# Set start/end date/time based on current date/time and set time period (30 days, in this instance)
timeDelta = timedelta(days=30)
currentDateTime = datetime.now()
startDateTime = currentDateTime - timeDelta

# Initialize data list with headers
data = [['Timestamp', 'Source IP', 'Destination IP', 'Event Type']]

# Generate 100 sample events
for i in range(100):
    generateEvent()

# Convert data to Pandas DataFrame and save as CSV
df = pd.DataFrame(data[1:], columns=data[0])
print("\n" + f"{df}")
df.to_csv('simulated_siem_events.csv', index=False)
print("\n" + "Data saved to simulated_siem_events.csv")