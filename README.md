# 🚀 SmartCity AI - Self-Healing ETL Pipeline

An AI-powered Smart City Data Engineering project that simulates real-world transportation data, detects data quality issues, automatically repairs recoverable records, and stores trusted data using a Medallion Architecture (Bronze → Silver → Gold).

---

# 📖 Project Overview

Modern Smart City platforms continuously collect operational data from multiple sources such as public transportation systems, emergency services, and IoT devices.

Poor data quality can negatively impact analytics, reporting, and AI models.

This project demonstrates how a modern Data Engineering pipeline can automatically identify, validate, and repair data quality issues before they reach downstream systems.

---

# ✨ Current Features

## Smart City Data Simulator

- Synthetic Bus GPS Dataset
- Emergency Incident Dataset
- Configurable Data Generator
- JSON & CSV Output

---

## Data Quality Testing Framework

Implemented test scenarios:

- Missing Zone
- Invalid GPS Coordinates
- Negative Delay
- Future Timestamp
- Duplicate Bus ID

Each scenario can be independently injected into the generated dataset to simulate real-world data quality problems.

---

# 🏗 Project Architecture

```
                Smart City Simulator
                        │
                        ▼
                 Raw Dataset Generation
                        │
                        ▼
           Data Quality Test Framework
                        │
                        ▼
               Bronze Layer (Upcoming)
                        │
                        ▼
             Validation & Rule Engine
                        │
                        ▼
             AI Self-Healing (Gemini)
                        │
                        ▼
                 Silver Layer
                        │
                        ▼
                  Gold Analytics
```

---

# 📂 Project Structure

```
SmartCity-AI-SelfHealing-ETL
│
├── config/
│     simulator_config.json
│
├── utils/
│     config.py
│
├── NoteBooks/
│     Bronze/
│         00_generate_datasets.ipynb
│         01_ingestion.ipynb
│
└── README.md
```

---

# 🛠 Technology Stack

- Python
- Pandas
- PySpark *(Upcoming)*
- Delta Lake *(Upcoming)*
- Databricks
- Git & GitHub
- Gemini AI *(Upcoming)*

---

# 📊 Data Simulation

Instead of downloading static datasets, this project generates synthetic Smart City operational data.

Current datasets include:

- Bus GPS Data
- Emergency Incident Data

Dataset generation is fully configurable through:

```
config/simulator_config.json
```

---

# 🧪 Data Quality Framework

The project currently supports the following data quality dimensions:

| Dimension | Test Scenario |
|-----------|---------------|
| Completeness | Missing Zone |
| Validity | Invalid GPS |
| Accuracy | Negative Delay |
| Timeliness | Future Timestamp |
| Uniqueness | Duplicate Bus ID |

---

# ▶️ How to Run

1. Clone the repository

2. Open the project in Databricks

3. Run

```
NoteBooks/Bronze/00_generate_datasets.ipynb
```

to generate Smart City datasets.

Future notebooks will automatically consume these datasets for the ETL pipeline.

---

# 🚧 Current Status

## Completed

- Smart City Simulator
- Data Quality Testing Framework

## In Progress

- Bronze Layer Ingestion

## Upcoming

- Schema Validation
- Rule Engine
- AI Self-Healing
- Silver Layer
- Gold Layer
- Monitoring Dashboard

---

# 📌 Project Roadmap

- [x] Smart City Data Simulator
- [x] Data Quality Framework
- [ ] Bronze Layer
- [ ] Validation Engine
- [ ] Rule Engine
- [ ] Gemini AI Integration
- [ ] Silver Layer
- [ ] Gold Layer
- [ ] Dashboard

---

# 👨‍💻 Author

**Mohammed Abdul Fawwaz**

Data Engineering Portfolio Project
