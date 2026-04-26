# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "5"
# ///
# Databricks notebook source

# COMMAND ----------
dbutils.widgets.text("env", "dev")
env = dbutils.widgets.get("env")

# COMMAND ----------

# COMMAND ----------
import os
from src.common.config_loader import load_config

BASE_PATH = os.path.dirname(os.getcwd())  # repo root

config = load_config(f"{BASE_PATH}/config/{env}.yml")

# COMMAND ----------

# COMMAND ----------
from src.common.spark_session import get_spark

spark = get_spark("bronze-customers")

# COMMAND ----------

# COMMAND ----------
from src.common.config_loader import load_config

config = load_config(f"{BASE_PATH}/config/{env}.yml")

customers_path = config["storage"]["customers_path"]

# COMMAND ----------

# COMMAND ----------
df_bronze = spark.read.format(config["format"]["input"]) \
    .option("header", config["options"]["header"]) \
    .option("inferSchema", config["options"]["inferSchema"]) \
    .load(customers_path)

# COMMAND ----------

# COMMAND ----------
df_bronze.display(limit=10)

# COMMAND ----------

# COMMAND ----------
from pyspark.sql.functions import current_timestamp

df_bronze = df_bronze.withColumn("ingestion_timestamp", current_timestamp())

# COMMAND ----------

table_name = f"{env}.01_bronze.{config['tables']['bronze_customers']}"

df_bronze.write.format("delta") \
    .mode("overwrite") \
    .saveAsTable(table_name)

# COMMAND ----------

spark.sql("DESCRIBE DETAIL workspace.default.dev_bronze_customers").select("location").show(truncate=False)

# COMMAND ----------


