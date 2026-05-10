# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "2"
# ///
from pyspark.sql.functions import current_timestamp

# COMMAND ----------

dbutils.widgets.text("catalog", "dev")
dbutils.widgets.text("schema", "bronze")
dbutils.widgets.text("customer_volume_path", "/Volumes/dev/00_landing_zone/01_managed_volume")

# COMMAND ----------

catalog = dbutils.widgets.get("catalog")
schema = dbutils.widgets.get("schema")
customer_volume_path = dbutils.widgets.get("customer_volume_path")

table_name = f"{catalog}.{schema}.customer_bronze"

# COMMAND ----------

df = spark.read.format("csv") \
    .option("header", True) \
    .option("inferSchema", True) \
    .load(customer_volume_path)

# COMMAND ----------

df = df.withColumn("ingestion_time", current_timestamp())

# COMMAND ----------

spark.sql(f"CREATE SCHEMA IF NOT EXISTS {catalog}.{schema}")

# COMMAND ----------

df.write.format("delta") \
    .mode("append") \
    .saveAsTable(table_name)

# COMMAND ----------

print(f"Loaded data into {table_name}")
