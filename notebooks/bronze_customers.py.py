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

BASE_PATH = "/Workspace/Repos/<user>/<repo>"

config = load_config(f"{BASE_PATH}/config/{env}.yml")

# COMMAND ----------

# COMMAND ----------
from src.common.spark_session import get_spark

spark = get_spark("bronze-customers")

# COMMAND ----------

# COMMAND ----------
base_path = config["storage"]["base_path"]
dataset = config["storage"]["datasets"]["customers"]

customers_path = f"{base_path}/{dataset['path']}"

# COMMAND ----------

# COMMAND ----------
df_bronze = spark.read.format(dataset["format"]) \
    .option("header", config["options"]["header"]) \
    .option("inferSchema", config["options"]["inferSchema"]) \
    .load(customers_path)

# COMMAND ----------

# COMMAND ----------
df_bronze.display()

# COMMAND ----------

# COMMAND ----------
from pyspark.sql.functions import current_timestamp

df_bronze = df_bronze.withColumn("ingestion_timestamp", current_timestamp())

# COMMAND ----------

# COMMAND ----------
df_bronze.write.format("delta") \
    .mode("overwrite") \
    .saveAsTable(config["tables"]["bronze"]["customers"])

# COMMAND ----------

# COMMAND ----------
print("Bronze customers table created successfully")

# COMMAND ----------

import os
print(os.getcwd())

# COMMAND ----------


