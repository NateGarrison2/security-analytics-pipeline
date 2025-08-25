# Import libraries
import datetime
from datetime import datetime, timedelta
import random

# Set start/end date/time based on current date/time and set time period (30 days, in this instance)
timeDelta = timedelta(days=30)
currentDateTime = datetime.now()
startDateTime = currentDateTime - timeDelta

# Function to generate random time between start date/time and end date/time
def generateRandomDateTime(start, end):
    timeDelta = end - start
    randomSeconds = random.uniform(0, timeDelta.total_seconds())
    return start + timedelta(seconds=randomSeconds)

# Function to generate random SIEM event type
def generateRandomEventType():
    eventTypes = ["loginSuccess",
                  "loginFailure",
                  "multipleLoginFailures",
                  "SSHBruteForceAttempt",
                  "XSSAttempt",
                  "firewallBlock",
                  "malwareDetected"]
    weights = [0.60, 
               0.15,
               0.05,
               0.10,
               0.05,
               0.04,
               0.01]
    return random.choices(eventTypes, weights)[0]

def assignEventGroup(eventType):
    groupAssignment = {
        "loginSuccess": "loginAttempt",
        "loginFailure": "loginAttempt",
        "multipleLoginFailures": "loginAttempt",
        "SSHBruteForceAttempt": "IDSAlert",
        "XSSAttempt": "IDSAlert",
        "firewallBlock": "firewallBlock",
        "malwareDetected": "malwareDetected"
    }
    return groupAssignment[eventType]

# Function to assign a severity level to the generated event type
def assignSeverity(eventType):
    severityAssignment = {
        "loginSuccess": "low", 
        "loginFailure": "medium",
        "multipleLoginFailures": "high",
        "XSSAttempt": "high", 
        "firewallBlock": "high", 
        "SSHBruteForceAttempt": "high",
        "malwareDetected": "critical"
    }
    return severityAssignment[eventType]

# Function to assign color to severity level to be printed in terminal
def assignColor(severityLevel):
    colorAssignment = {
        "low": '\033[32m', # Green
        "medium": '\033[33m', # Yellow
        "high": '\033[31m', # Red
        "critical": '\033[41m' # Highlighted red
    }
    return colorAssignment[severityLevel]

# Function to generate a random source IPv4 (public range)
def generateRandomSourceIPv4():
    return ".".join(str(random.randint(0, 255)) for i in range(4))

# Function to generate a random destination IPv4 (large private range)
def generateRandomDestIPv4():
    return "10." + ".".join(str(random.randint(0, 255)) for i in range(3))

def generateEvent():
    eventDateTime = generateRandomDateTime(startDateTime, currentDateTime)
    sourceIP = generateRandomSourceIPv4()
    destIP = generateRandomDestIPv4()
    eventType = generateRandomEventType()
    eventGroup = assignEventGroup(eventType)
    severityLevel = assignSeverity(eventType)
    print(f"\nEvent date and time: {eventDateTime}")
    print(f"Source IPv4: {sourceIP}")
    print(f"Destination IPv4: {destIP}")
    print(f"Event type: {eventType}")
    print(f"Event group: {eventGroup}")
    print(f"Event severity level: " + assignColor(severityLevel) + f"{severityLevel}" + '\033[0m')
    
for i in range(10):
    generateEvent()