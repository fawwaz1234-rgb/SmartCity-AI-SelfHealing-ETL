# Simulator Configuration

BUS_RECORDS = 10000
EMERGENCY_RECORDS = 8000

ANOMALY_PERCENTAGE = 10

RANDOM_SEED = 42

ZONES = [
    "Zone A",
    "Zone B",
    "Zone C",
    "Zone D",
    "Zone E"
]

ROUTES = [
    "R101",
    "R102",
    "R103",
    "R104",
    "R105"
]

INCIDENT_TYPES = [
    "Accident",
    "Fire",
    "Medical",
    "Road Block",
    "Power Failure"
]

# -----------------------------
# Project Paths
# -----------------------------

import os

PROJECT_ROOT = os.path.abspath("/Workspace/Users/mabd95026@gmail.com/SmartCity-AI-SelfHealing-ETL")

RAW_PATH = os.path.join(PROJECT_ROOT, "Data", "raw")
BRONZE_PATH = os.path.join(PROJECT_ROOT, "Data", "bronze")
SILVER_PATH = os.path.join(PROJECT_ROOT, "Data", "silver")
GOLD_PATH = os.path.join(PROJECT_ROOT, "Data", "gold")
QUARANTINE_PATH = os.path.join(PROJECT_ROOT, "Data", "quarantine")
LOG_PATH = os.path.join(PROJECT_ROOT, "Data", "logs")