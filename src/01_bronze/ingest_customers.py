from src.common.spark_session import get_spark

def load_customers(path):
    spark = get_spark()
    return spark.read.format("delta").load(path)
