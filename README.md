# 🚀 Smart City AI Self-Healing ETL Pipeline

![Python](https://img.shields.io/badge/Python-3.11-blue)
![PySpark](https://img.shields.io/badge/PySpark-3.5-orange)
![Databricks](https://img.shields.io/badge/Databricks-Community-red)
![Spark SQL](https://img.shields.io/badge/Spark_SQL-Analytics-success)
![Architecture](https://img.shields.io/badge/Architecture-Medallion-success)
![AI](https://img.shields.io/badge/AI-Gemini%20%2B%20Groq-purple)
![Status](https://img.shields.io/badge/Status-Version%201.0-brightgreen)

---

## 📖 Project Overview

Smart City platforms generate millions of records every day from emergency services, transportation systems, traffic monitoring, weather stations, and IoT devices.

Poor data quality directly affects analytics, dashboards, and operational decisions.

This project demonstrates an **AI-Powered Self-Healing ETL Pipeline** built using **PySpark**, **Databricks**, and **Large Language Models (Gemini + Groq)**.

Instead of rejecting invalid records, the pipeline automatically:

- Ingests raw Smart City datasets
- Validates incoming records
- Quarantines invalid records
- Repairs missing values using AI
- Routes low-confidence predictions for human review
- Merges trusted repairs back into the Silver Layer
- Generates business-ready Gold Layer datasets

The project follows the **Medallion Architecture (Bronze → Silver → Gold)** commonly used in modern Data Engineering platforms.

---

# 🏗️ Architecture

> Replace this placeholder with `architecture.png`

```text
                    Smart City Data Sources

      CSV                    CSV                  API (Future)
       │                      │                       │
       └──────────────┬───────┴───────────────────────┘
                      │
                      ▼
              🥉 Bronze Layer
          Raw Data Ingestion
                      │
                      ▼
              🥈 Silver Layer
      Validation • Cleaning • Standardization
                      │
          ┌───────────┴─────────────┐
          ▼                         ▼
    Valid Records            Quarantine
                                   │
                                   ▼
                    🤖 AI Repair Agent
                  Gemini → Groq Router
                                   │
                    ┌──────────────┴──────────────┐
                    ▼                             ▼
            Auto Approved                 Human Review
                    │
                    ▼
          Updated Silver Dataset
                    │
                    ▼
              🥇 Gold Analytics
                    │
                    ▼
         📊 Dashboard (Coming Soon)
```

---

# 🎯 Objectives

- Build an End-to-End ETL Pipeline
- Implement Medallion Architecture
- Validate Smart City datasets
- Repair missing values using AI
- Automate confidence-based approval
- Generate Gold Layer analytics
- Demonstrate production-inspired Data Engineering practices

---

# 📂 Current Datasets

## ✅ Emergency Incident Dataset

Contains:

- Incident ID
- Zone
- Incident Type
- Severity
- Response Time
- Status
- Timestamp

Used for:

- Data Validation
- AI Repair
- Incident Analytics
- Response Time Analysis
- Zone Analysis

---

## ✅ Bus GPS Dataset

Contains:

- Bus ID
- Route ID
- Latitude
- Longitude
- Delay Minutes
- Timestamp

Used for:

- Delay Analysis
- Route Analytics
- Transportation KPIs

---

# 🚧 Planned Datasets

| Dataset | Purpose |
|----------|----------|
| Traffic Flow | Congestion Analysis |
| Weather API | Weather Impact Analysis |
| Air Quality | Pollution Monitoring |

---

# 🛠️ Technology Stack

## Languages

- Python
- SQL

## Big Data

- PySpark
- Spark SQL
- Databricks

## Storage

- Parquet

## AI

- Gemini API
- Groq API

## Libraries

- Pandas
- NumPy

## Version Control

- Git
- GitHub

---

# 📁 Repository Structure

```text
SmartCity-AI-SelfHealing-ETL

│
├── notebooks
│
│   ├── Bronze
│   │      00_generate_datasets.ipynb
│   │      01_ingestion.ipynb
│   │
│   ├── Silver
│   │      02_silver_processing.ipynb
│   │
│   ├── AI
│   │      03_ai_repair_agent.ipynb
│   │
│   └── Gold
│          04_gold_layer.ipynb
│
├── config
│
├── utils
│
├── requirements.txt
│
├── README.md
│
└── LICENSE
```

---

# ⚙️ ETL Workflow

## 🥉 Bronze Layer

Responsibilities

- Raw Data Ingestion
- Schema Validation
- Metadata Generation
- Parquet Storage

---

## 🥈 Silver Layer

Responsibilities

- Data Cleaning
- Validation Rules
- Standardization
- Duplicate Removal
- Null Handling
- Quarantine Generation

---

## 🤖 AI Repair Layer

Responsibilities

- Analyze quarantined records
- Infer missing values
- Confidence scoring
- Gemini API
- Groq fallback
- Auto approval
- Human review routing
- Merge approved records into Silver

---

## 🥇 Gold Layer

Responsibilities

- Business KPIs
- Aggregated datasets
- Dashboard-ready tables
- Analytics

---

# 🤖 AI Self-Healing Workflow

```text
Quarantined Record

        │

        ▼

 Gemini API

        │

 Success ?

    │        │

   Yes      No

    │        │

    ▼        ▼

 Gemini    Groq

      │

      ▼

 Confidence Score

      │

 ┌────┴────┐

 ▼         ▼

Auto     Human

Approve  Review

      │

      ▼

Updated Silver Layer
```

---

# 📊 Gold Layer Outputs

The pipeline currently generates the following business-ready datasets.

### Emergency Analytics

- Emergency Incident Summary
- Incident Status Summary
- Response Time Analysis
- Zone Severity Analysis

### Transportation Analytics

- Bus Delay Summary

### AI Analytics

- AI Repair Summary

---



# 🚀 Installation

Clone repository

```bash
git clone https://github.com/fawwaz1234-rgb/SmartCity-AI-SelfHealing-ETL.git
```

Install requirements

```bash
pip install -r requirements.txt
```

---

# 🔑 Configure API Keys

Create

```
config/

gemini_config.py

groq_config.py
```

Example

```python
GEMINI_API_KEY="YOUR_API_KEY"

GROQ_API_KEY="YOUR_API_KEY"
```

---

# ▶️ Execute Pipeline

Run notebooks in order

```text
Bronze

↓

Silver

↓

AI Repair

↓

Gold
```

---

# 📈 Features

✔ Medallion Architecture

✔ AI Self-Healing

✔ PySpark ETL

✔ Databricks

✔ Spark SQL

✔ Data Validation

✔ Data Cleaning

✔ Quarantine Layer

✔ Gemini Integration

✔ Groq Fallback

✔ Confidence-Based Approval

✔ Automated Silver Repair

✔ Gold Layer Analytics

✔ Modular Notebook Architecture

---

# 💼 Skills Demonstrated

- Data Engineering
- ETL Development
- PySpark
- Spark SQL
- Databricks
- AI Integration
- LLM Routing
- Data Validation
- Data Cleaning
- Data Quality Engineering
- Gold Layer Analytics
- Git & GitHub

---

# 🚀 Project Roadmap

## Version 1.1

- ✅ Interactive Power BI Dashboard
- ✅ Gold Layer Visualizations
- ✅ KPI Dashboard

---

## Version 1.2

- Weather API Integration
- Traffic Flow Dataset
- Air Quality Dataset
- Additional Gold Layer KPIs

---

## Version 2.0

- Real-Time Streaming Pipeline
- Apache Kafka Integration
- Automated ETL Scheduling
- Monitoring Dashboard
- Data Quality Alerts
- Multi-model AI Support

---

# 📊 Planned Dashboard

The Power BI Dashboard will include:

- Emergency Incident Dashboard
- Bus Delay Dashboard
- AI Repair Dashboard
- Response Time Analysis
- Zone Heatmap
- Incident Trend Analysis
- Data Quality KPIs
- AI Approval Statistics

---

# 🌐 Planned API Integration

Future versions will integrate:

- Weather API
- Traffic API
- Smart City IoT API

These APIs will provide live operational data for real-time analytics.

---

# 🔮 Future Vision

Transform this project into a complete Smart City Analytics Platform capable of:

- Processing multiple city datasets
- AI-assisted automated data repair
- Live dashboard reporting
- Streaming analytics
- Production deployment
- Enterprise-scale monitoring

---

# 🤝 Contributing

Contributions are welcome.

Feel free to submit issues, feature requests, or pull requests.

---

# 📄 License

Licensed under the MIT License.

---

# ⭐ Author

**Mohammed Abdul Fawwaz**

Aspiring Data Engineer | PySpark | Databricks | AI-powered Data Engineering

GitHub:
https://github.com/fawwaz1234-rgb

---

⭐ If you found this project useful, consider giving it a star!
