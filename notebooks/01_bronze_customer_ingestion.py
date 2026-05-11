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
dbutils.widgets.text("checkpoint_path", "")
dbutils.widgets.text("schema_location", "")

# COMMAND ----------

catalog = dbutils.widgets.get("catalog")
schema = dbutils.widgets.get("schema")
customer_volume_path = dbutils.widgets.get("customer_volume_path")
checkpoint_path = dbutils.widgets.get("checkpoint_path")
schema_location = dbutils.widgets.get("schema_location")

table_name = f"{catalog}.{schema}.customer_bronze"


# COMMAND ----------

df = (spark.readStream
    .format("cloudFiles")
    .option("cloudFiles.format", "csv")
    .option("cloudFiles.schemaLocation", schema_location)
    .option("cloudFiles.inferColumnTypes", "true")
    .option("header", "true")
    .load(customer_volume_path))


# COMMAND ----------

# Cell 5: Professional Metadata Extraction
from pyspark.sql.functions import current_timestamp

df = df.select(
    "*", 
    "_metadata.file_path", 
    "_metadata.file_modification_time"
).withColumnRenamed("file_path", "source_file") \
 .withColumn("ingestion_time", current_timestamp())


# COMMAND ----------

spark.sql(f"CREATE SCHEMA IF NOT EXISTS {catalog}.{schema}")

# COMMAND ----------

query = (df.writeStream
    .format("delta")
    .outputMode("append")
    .option("checkpointLocation", checkpoint_path)
    .option("mergeSchema", "true")
    .trigger(availableNow=True)
    .toTable(table_name))

query.awaitTermination()


# COMMAND ----------

print(f"Loaded data into {table_name}")

# COMMAND ----------

display(spark.table(table_name))


# COMMAND ----------


