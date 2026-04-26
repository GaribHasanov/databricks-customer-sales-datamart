from pyspark.sql.functions import col

def clean_customers(df):
    return df.dropna().dropDuplicates()
