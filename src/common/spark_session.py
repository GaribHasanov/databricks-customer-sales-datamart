from pyspark.sql import SparkSession

def get_spark(app_name: str = "CustomerSalesMedallion"):
    spark = SparkSession.builder \
        .appName(app_name) \
        .config("spark.sql.shuffle.partitions", "200") \
        .config("spark.sql.adaptive.enabled", "true") \
        .getOrCreate()

    return spark
