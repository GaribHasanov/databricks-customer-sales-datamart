# databricks-customer-sales-datamart

## Architecture
- Bronze: Raw ingestion
- Silver: Cleaned & standardized data
- Gold: Business data marts

## Tech Stack
- Databricks
- PySpark
- Delta Lake

## Structure
src/ -> business logic
jobs/ -> pipeline entry points
configs/ -> environment configs


# End-to-End Data Engineering Pipeline (Databricks + CI/CD)

## 📌 Project Overview
This project demonstrates a complete end-to-end data engineering pipeline built on **Databricks** using a Medallion Architecture (Bronze, Silver, Gold). It includes automated data ingestion, transformation, testing, and CI/CD deployment using GitHub Actions.

The goal of this project is to simulate a real-world production-grade data pipeline used in modern data platforms.

---

## 🏗️ Architecture

The pipeline follows a layered approach:

- **Bronze Layer** → Raw data ingestion from source systems
- **Silver Layer** → Cleaned and validated data
- **Gold Layer** → Business-ready aggregated data for analytics & reporting

---

## ⚙️ Tech Stack

- Databricks
- Apache Spark (PySpark)
- SQL
- Python
- GitHub Actions (CI/CD)
- Delta Lake
- YAML-based configuration
- Pytest (unit testing)

---

## 🚀 Features

- Automated ETL pipeline (Extract, Transform, Load)
- Medallion architecture implementation (Bronze → Silver → Gold)
- Modular and reusable job structure
- Schema management and validation
- CI/CD pipeline using GitHub Actions
- Unit testing for data quality checks
- Config-driven pipeline execution
- Databricks job orchestration

---

## 📂 Project Structure
