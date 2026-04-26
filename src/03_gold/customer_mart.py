from pyspark.sql.functions import count

def customer_summary(df):
    return df.groupBy("customer_id").agg(count("*").alias("total_orders"))
