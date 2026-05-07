# End-to-End Data Engineering Pipeline (Sales & Customers) | Databricks | CI/CD

## Project Overview
This project is an end-to-end data engineering pipeline built on Databricks using a **Sales & Customers dataset**. It demonstrates how raw transactional and customer data is ingested, transformed, and modeled into analytics-ready datasets using a Medallion Architecture (Bronze, Silver, Gold).

The project also includes CI/CD automation using GitHub Actions for deployment and testing.

---

## Architecture

The pipeline follows a Medallion Architecture:

- **Bronze Layer** → Raw sales and customer data ingestion
- **Silver Layer** → Cleaned, validated, and joined datasets (orders + customers)
- **Gold Layer** → Business-ready analytical tables (KPIs, revenue, customer insights)

---

## Tech Stack

- Databricks
- Apache Spark (PySpark)
- SQL
- Python
- Delta Lake
- GitHub Actions (CI/CD)
- Pytest

---

## Key Features

- End-to-end ETL pipeline (Sales & Customers domain)
- Medallion architecture implementation (Bronze / Silver / Gold)
- Data cleaning, deduplication, and validation
- Customer-order data integration (joins)
- Business KPI generation (revenue, order counts, customer metrics)
- Config-driven pipeline design
- Automated CI/CD deployment via GitHub Actions
- Unit testing for data quality checks

---

## Project Structure

.github/workflows → CI/CD pipelines (GitHub Actions)  
config → Environment and pipeline configurations  
jobs → ETL job definitions (Bronze/Silver/Gold logic)  
notebooks → Development and exploratory analysis  
resources/schemas → Data schemas for validation  
src → Core transformation logic (PySpark / SQL)  
tests → Unit tests for data quality  
databricks.yml → Databricks deployment configuration  
requirements.txt → Python dependencies  

---

## Data Model

### Source Tables
- Sales Orders (transactions)
- Customers (customer master data)

### Transformations
- Data cleaning (null handling, type casting)
- Customer-order joins
- Aggregations for KPIs

### Final Outputs
- Total revenue per period
- Customer lifetime value (CLV)
- Order frequency metrics
- Top customers by revenue

---

## Pipeline Flow

1. Raw sales and customer data ingested into Bronze layer  
2. Data is cleaned and standardized in Silver layer  
3. Customers and orders are joined and validated  
4. Business logic applied in Gold layer (KPIs, aggregations)  
5. Final datasets are made ready for BI tools (e.g., Power BI)

---

## CI/CD Process

- GitHub Actions triggers pipeline on push
- Databricks jobs are deployed automatically
- Tests are executed before deployment
- Environment variables managed securely

---

## Testing Strategy

- Unit tests using Pytest
- Schema validation tests
- Data quality checks (nulls, duplicates, integrity)
- Pipeline validation for Bronze → Silver → Gold flow

---

## Key Learnings

- Designing scalable ETL pipelines
- Implementing Medallion Architecture
- Working with Databricks and Delta Lake
- Building production-style CI/CD workflows
- Data modeling for business analytics

---

## Future Improvements

- Add real-time streaming ingestion (Kafka)
- Implement advanced data quality framework
- Add monitoring & alerting layer
- Extend orchestration with Databricks Workflows / Airflow

---

## Author

Garib Hasanov  
Data Engineering / Analytics Engineering Portfolio Project
