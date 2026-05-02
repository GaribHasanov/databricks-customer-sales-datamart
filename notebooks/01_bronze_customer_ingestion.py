# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "2"
# ///
from pyspark.sql.functions import current_timestamp

# ---------------------------
# BUNDLE CONFIG (runtime parameters)
# ---------------------------

dbutils.widgets.text("catalog", "dev")
dbutils.widgets.text("schema", "01_bronze")
dbutils.widgets.text("customer_volume_path", "/Volumes/dev/00_landing_zone/01_managed_volume")

catalog = dbutils.widgets.get("catalog")
schema = dbutils.widgets.get("schema")
customer_volume_path = dbutils.widgets.get("customer_volume_path")

table_name = f"{catalog}.{schema}.customer_bronze"

# ---------------------------
# READ RAW DATA
# ---------------------------
df = spark.read.format("csv") \
    .option("header", True) \
    .option("inferSchema", True) \
    .load(customer_volume_path)

# ---------------------------
# BRONZE ENRICHMENT
# ---------------------------
df = df.withColumn("ingestion_time", current_timestamp())

# ---------------------------
# WRITE TO DELTA BRONZE
# ---------------------------
df.write.format("delta") \
    .mode("append") \
    .saveAsTable("dev.01_bronze.customer_bronze")

print(f"Loaded data into {table_name}")

# COMMAND ----------


