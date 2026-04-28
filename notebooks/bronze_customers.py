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

import sys
import os

# cari notebook/script harada işləyirsə, oradan yuxarı qalxıb src tap
current = os.getcwd()

while current != "/":
    if os.path.exists(os.path.join(current, "src")):
        sys.path.insert(0, current)
        break
    current = os.path.dirname(current)

# COMMAND ----------

# COMMAND ----------
from src.common.config_loader import load_config
from src.common.spark_session import get_spark

spark = get_spark("bronze-customers")

# COMMAND ----------

# COMMAND ----------
from src.common.config_loader import load_config

config = load_config(f"{BASE_PATH}/config/{env}.yml")

customers_path = config["storage"]["customers_path"]
#customers_path = config["storage"]["datasets"]["customers"]["path"]

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
