from pyspark.sql import SparkSession


def get_spark(app_name="customer-sales-pipeline"):
    return (
        SparkSession.builder
        .appName(app_name)
        .config("spark.sql.adaptive.enabled", "true")
        .config("spark.sql.shuffle.partitions", "200")
        .getOrCreate()
    )
